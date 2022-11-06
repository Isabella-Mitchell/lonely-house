from django.conf import settings
# think I can remove this import


def cart_contents(request):

    cart_items = []
    total = 0
    listing_count = 0

    context = {
        'cart_items':  cart_items,
        'total': total,
        'listing_count': listing_count,
    }

    return context
