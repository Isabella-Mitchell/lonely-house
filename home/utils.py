
from listings.models import Listing, Category
from reviews.models import Review


def get_featured(model, number_of_instances):
    """A view to return all featured listings or categories"""

    instances = model.objects.all()
    featured_instances = instances.filter(featured=True)
    # limits returned instances to three. Will show oldest first.
    no_featured_instances = featured_instances[:number_of_instances]

    return no_featured_instances
