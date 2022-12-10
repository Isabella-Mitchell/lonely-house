from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from listings.models import Listing
from .utils import dates_string_to_list


def view_cart(request):
    """A view to renders the cart contents page"""

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """Add the listing booking details to the cart"""

    listing = get_object_or_404(Listing, pk=item_id)
    start_date = request.POST.get('startDate')
    end_date = request.POST.get('endDate')
    selected_dates = dates_string_to_list(request.POST.get('selected-dates-array-input'))
    no_nights = int(request.POST.get('selected-no-nights-input'))
    # Nice to have - make it easier for users to nav back to the listing page to amend booking
    # redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    # walkthrough has a if else statement here for quantity selector
    cart[item_id] = {
        'no_nights': no_nights,
        'selected_dates': selected_dates,
        'start_date': start_date,
        'end_date': end_date,
    }
    messages.success(request, f'Added {listing.name} to your cart')

    request.session['cart'] = cart
    return render(request, 'cart/cart.html')


def remove_from_cart(request, item_id):
    """Removes the listing booking details from the cart"""

    listing = get_object_or_404(Listing, pk=item_id)
    cart = request.session.get('cart', {})

    try:
        cart.pop(item_id)

        request.session['cart'] = cart
        messages.success(request, f'Removed {listing.name} from your cart')
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item {e}')
        return HttpResponse(status=500)
