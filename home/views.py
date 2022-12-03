from django.shortcuts import render
import datetime
from datetime import date, timedelta
from listings.models import Listing, Category


def get_featured(model):
    """A view to return all featured listings or categories"""

    instances = model.objects.all()
    featured_instances = instances.filter(featured=True)
    # limits returned instances to three. Will show oldest first.
    three_featured_instances = featured_instances[:3]

    return three_featured_instances


def index(request):
    """A view to return the index page including featured content"""

    featured_listings = get_featured(Listing)
    featured_categories = get_featured(Category)

    context = {
        'featured_listings': featured_listings,
        'featured_categories': featured_categories,
    }

    return render(request, 'home/index.html', context)
