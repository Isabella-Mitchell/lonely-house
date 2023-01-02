from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.http import QueryDict
from .models import Listing, Category, Image, Facility
from .constants import sleep_filters_constant
from checkout.models import OrderLineItem
from reviews.models import Review
from .utils import get_filters, get_listing_reviews
from reviews.utils import (
    get_average_ratings, get_single_listing_average_rating)


def all_listings(request):
    """A view to return all listings including sorting and search queries"""

    listings = Listing.objects.all()
    total_number_of_listings = listings.count
    query = None
    sleeps_query = None
    categories_query = None
    facilities_query = None

    average_ratings = get_average_ratings(listings)

    category_filters = get_filters(Category)
    sleep_filters = sleep_filters_constant
    facility_filters = get_filters(Facility)

    if request.GET:

        if 'category' in request.GET:
            category_query = request.GET.getlist('category')
            listings = listings.filter(category__name__in=category_query)
            categories_query = Category.objects.filter(name__in=category_query)

        if 'sleeps' in request.GET:
            sleeps_query = request.GET.getlist('sleeps')
            # TO DO - Could also be gte instead of in
            listings = listings.filter(no_sleeps__in=sleeps_query)

        if 'facility' in request.GET:
            facility_query = request.GET.getlist('facility')
            listings = listings.filter(
                facilities__name__in=facility_query).distinct()
            facilities_query = Facility.objects.filter(name__in=facility_query)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('listings'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query) | Q(
                region__icontains=query) | Q(
                country__icontains=query)
            listings = listings.filter(queries)

    context = {
        'listings': listings,
        'total_number_of_listings': total_number_of_listings,
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

    average_rating = get_single_listing_average_rating(listing_id)

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
        'average_rating': average_rating,
    }

    return render(request, 'listings/listing_detail.html', context)


def bug_fix(request):
    """A view to return the index page including featured content"""

    return render(request, 'listings/bug_fix.html')
