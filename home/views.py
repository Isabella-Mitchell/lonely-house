from django.shortcuts import render
import datetime
from datetime import date, timedelta
from listings.models import Listing, Category
from reviews.models import Review


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
    featured_reviews = get_featured(Review)

    context = {
        'featured_listings': featured_listings,
        'featured_categories': featured_categories,
        'featured_reviews': featured_reviews,
    }

    return render(request, 'home/index.html', context)
