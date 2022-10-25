from django.shortcuts import render
from .models import Listing


def all_listings(request):
    """A view to return all listings including sorting and search queries"""

    listings = Listing.objects.all()

    context = {
        'listings': listings,
    }

    return render(request, 'listings/listings.html', context)
