from django.shortcuts import render, redirect, HttpResponse


def view_cart(request):
    """A view to renders the cart contents page"""

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """Add the listing booking details to the cart"""

    start_date = request.POST.get('startDate')
    end_date = request.POST.get('endDate')
    no_nights = int(request.POST.get('selected-no-nights-input'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    # walkthrough has a if else statement here for quantity selector
    if item_id in list(cart.keys()):
        cart[item_id] = {
            'no_nights': no_nights,
            'start_date': start_date,
            'end_date': end_date,
        }
    else:
        cart[item_id] = {
            'no_nights': no_nights,
            'start_date': start_date,
            'end_date': end_date,
        }

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """Removes the listing booking details from the cart"""

    cart = request.session.get('cart', {})

    try:
        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
