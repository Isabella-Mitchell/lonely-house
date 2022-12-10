from .models import Listing, Category, Image, Facility
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


def get_listing_reviews(listing_id):
    reviews = Review.objects.all()
    listing_reviews = reviews.filter(listing_id=listing_id)
    return listing_reviews
