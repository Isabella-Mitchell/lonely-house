from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.http import QueryDict
from .models import Listing, Category, Image, Facility
from checkout.models import OrderLineItem


def all_listings(request):
    """A view to return all listings including sorting and search queries"""

    listings = Listing.objects.all()
    query = None
    sleeps_query = None
    categories_query = None
    facilities_query = None

    category_filters = [{
        'name': 'wetlands',
        'friendly_name': 'Wetlands',
    }, {
        'name': 'forest',
        'friendly_name': 'Forest',
    }]
    sleep_filters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    facility_filters = [{
        'name': 'dog_friendly',
        'friendly_name': 'Dog Friendly'
    }, {
        'name': 'wheelchair_accessible',
        'friendly_name': 'Wheelchair Accessible'
    }]

    if request.GET:

        if 'category' in request.GET:
            category_query = request.GET.getlist('category')
            listings = listings.filter(category__name__in=category_query)
            categories_query = Category.objects.filter(name__in=category_query)

        if 'sleeps' in request.GET:
            # # gte means greater than or equal too
            # listings = listings.filter(no_sleeps__gte=sleeps_query)
            sleeps_query = request.GET.getlist('sleeps')
            listings = listings.filter(no_sleeps__in=sleeps_query)

        if 'facility' in request.GET:
            facilities_query = request.GET.getlist('facility')
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
        'sleeps_query': sleeps_query,
        'facilities_query': facilities_query,
        'category_filters': category_filters,
        'sleep_filters': sleep_filters,
        'facility_filters': facility_filters,
    }

    return render(request, 'listings/listings.html', context)


def listing_detail(request, listing_id):
    """A view to show individual listing details"""

    listing = get_object_or_404(Listing, pk=listing_id)

    listing_bookings = []

    # Getting Booked Dates from Orders. Passing into JS via template variable.
    all_bookings = OrderLineItem.objects.all()
    listing_bookings_filtered = all_bookings.filter(listing_id=listing_id)
    for item in listing_bookings_filtered:
        # to string for js. Otherwise would be a date object.
        booked_date = str(item.date)
        listing_bookings.append(booked_date)

    context = {
        'listing': listing,
        'listing_bookings': listing_bookings,
    }

    return render(request, 'listings/listing_detail.html', context)
