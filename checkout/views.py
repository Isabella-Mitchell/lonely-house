from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('listings'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51M2torGEB35ew8vJVkT33OPrZAWpdw2tUPO1FlvyzYa5D0kB7uuO4cvtN39EXyo1oUe41q3GV3GraUfs4jDudlB2009xD6IQkx',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
