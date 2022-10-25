from django.shortcuts import render, get_object_or_404
from .models import Listing


def all_listings(request):
    """A view to return all listings including sorting and search queries"""

    listings = Listing.objects.all()

    context = {
        'listings': listings,
    }

    return render(request, 'listings/listings.html', context)


def listing_detail(request, listing_id):
    """A view to show individual listing details"""

    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing,
    }

    return render(request, 'listings/listing_detail.html', context)
