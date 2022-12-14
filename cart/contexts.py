from django.conf import settings
from django.shortcuts import get_object_or_404
from listings.models import Listing


def cart_contents(request):

    cart_items = []
    subtotal = 0
    total = 0
    listing_count = 0
    cart = request.session.get('cart', {})

    for item_id, booking_details in cart.items():
        listing = get_object_or_404(Listing, pk=item_id)
        subtotal += booking_details['no_nights'] * listing.price
        listing_count += 1
        cart_items.append({
            'item_id': item_id,
            'no_nights': booking_details['no_nights'],
            'start_date': booking_details['start_date'],
            'end_date': booking_details['end_date'],
            'selected_dates': booking_details['selected_dates'],
            'listing': listing,
        })

    total = subtotal

    context = {
        'cart_items':  cart_items,
        'total': total,
        'listing_count': listing_count,
    }

    return context
