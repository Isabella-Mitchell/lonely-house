from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q, Avg
from django.http import QueryDict
from .models import Listing, Category, Image, Facility
from checkout.models import OrderLineItem
from reviews.models import Review


def get_filters(model):
    """Gets content from database to populate drop down filters"""

    filter_list = []
    get_instances = model.objects.all()
    for item in get_instances:
        newdict = {
            "name": item.name,
            "friendly_name": item.friendly_name}
        filter_list.append(newdict)
    return filter_list


def get_average_ratings(listings):
    """ Gets reviews. To update ny adding listing logic """
    reviews = Review.objects.all()
    rating_aggregates = []
    for listing in listings:
        filtered_reviews = reviews.filter(listing=listing)
        get_avg_rating = filtered_reviews.aggregate(Avg('rating'))
        if get_avg_rating['rating__avg'] is not None:
            newdict = {
                "listing": listing.name,
                "rating": get_avg_rating['rating__avg'],
            }
            rating_aggregates.append(newdict)
    return rating_aggregates


def get_listing_reviews(listing_id):
    reviews = Review.objects.all()
    listing_reviews = reviews.filter(listing_id=listing_id)
    return listing_reviews


def all_listings(request):
    """A view to return all listings including sorting and search queries"""

    listings = Listing.objects.all()
    query = None
    sleeps_query = None
    categories_query = None
    facilities_query = None

    average_ratings = get_average_ratings(listings)

    category_filters = get_filters(Category)
    sleep_filters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    facility_filters = get_filters(Facility)

    if request.GET:

        if 'category' in request.GET:
            category_query = request.GET.getlist('category')
            listings = listings.filter(category__name__in=category_query)
            categories_query = Category.objects.filter(name__in=category_query)

        if 'sleeps' in request.GET:
            sleeps_query = request.GET.getlist('sleeps')
            # Could also be gte instead of in (greater than or equal too)
            listings = listings.filter(no_sleeps__in=sleeps_query)

        # also check if this is what's causing multiples of same listings
        if 'facility' in request.GET:
            facility_query = request.GET.getlist('facility')
            listings = listings.filter(facilities__name__in=facility_query)
            facilities_query = Facility.objects.filter(name__in=facility_query)

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
        'average_ratings': average_ratings,
    }

    return render(request, 'listings/listings.html', context)


def listing_detail(request, listing_id):
    """A view to show individual listing details"""

    listing = get_object_or_404(Listing, pk=listing_id)

    reviews = get_listing_reviews(listing_id)

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
        'reviews': reviews,
    }

    return render(request, 'listings/listing_detail.html', context)
