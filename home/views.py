from django.shortcuts import render
from listings.models import Listing, Category
from reviews.models import Review
from .utils import get_featured
from reviews.utils import get_average_ratings, get_single_listing_average_rating


def index(request):
    """A view to return the index page including featured content"""

    featured_listings = get_featured(Listing, 3)
    featured_categories = get_featured(Category, 3)
    featured_reviews = get_featured(Review, 4)

    print(featured_listings)

    average_ratings = get_average_ratings(featured_listings)

    context = {
        'featured_listings': featured_listings,
        'average_ratings': average_ratings,
        'featured_categories': featured_categories,
        'featured_reviews': featured_reviews,
    }

    return render(request, 'home/index.html', context)
