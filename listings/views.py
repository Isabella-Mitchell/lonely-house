from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
# from django.http import QueryDict
from .models import Listing, Category, Image, Facility


def all_listings(request):
    """A view to return all listings including sorting and search queries"""

    listings = Listing.objects.all()
    query = None
    sleeps_query = None
    categories_query = None
    categories_query_name = None
    facilities_query = None
    facilities_query_name = None

    if request.GET:

        if 'category' in request.GET:
            category_list = request.GET['category']
            print(category_list)
            categories_query_name = request.GET['category']
            print(categories_query_name)
            categories_query = request.GET['category'].split(',')
            listings = listings.filter(category__name__in=categories_query)
            categories_query = Category.objects.filter(name__in=categories_query)

        if 'sleeps' in request.GET:
            sleeps_query = request.GET['sleeps']
            listings = listings.filter(no_sleeps=sleeps_query)

        if 'facility' in request.GET:
            facilities_query_name = request.GET['facility']
            facilities_query = request.GET['facility'].split(',')
            listings = listings.filter(facilities__name__in=facilities_query)
            facilities_query = Facility.objects.filter(name__in=facilities_query)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('listings'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            listings = listings.filter(queries)

    context = {
        'listings': listings,
        'search_term': query,
        'categories_query': categories_query,
        'categories_query_name': categories_query_name,
        'sleeps_query': sleeps_query,
        'facilities_query': facilities_query,
        'facilities_query_name': facilities_query_name,
    }

    return render(request, 'listings/listings.html', context)


def listing_detail(request, listing_id):
    """A view to show individual listing details"""

    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing,
    }

    return render(request, 'listings/listing_detail.html', context)
