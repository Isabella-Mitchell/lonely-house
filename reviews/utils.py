from listings.models import Listing
from django.db.models import Avg
from .models import Review


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
                "rating": round(get_avg_rating['rating__avg'], 1),
            }
            rating_aggregates.append(newdict)
    return rating_aggregates


def get_single_listing_average_rating(listing_id):
    reviews = Review.objects.all()
    filtered_reviews = reviews.filter(listing_id=listing_id)
    get_avg_rating = filtered_reviews.aggregate(Avg('rating'))
    if get_avg_rating['rating__avg'] is not None:
        rating = round(get_avg_rating['rating__avg'], 1)
        print(rating)
        return rating
