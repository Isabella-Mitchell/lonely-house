from django.shortcuts import render, redirect


def view_cart(request):
    """A view to renders the cart contents page"""

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """Add the dates of the specified listing to the shopping bag"""
    print("I'm adding to bag")

    start_date = request.POST.get('startDate')
    print(start_date)
    end_date = request.POST.get('endDate')
    print(end_date)
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    print(cart)

    # walkthrough has a if else statement here for quantity selector
    if item_id in list(cart.keys()):
        cart[item_id] = [start_date, end_date]
    else:
        cart[item_id] = [start_date, end_date]

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)
