from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from listings.models import Listing
from profiles.models import UserProfile

import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request
        print("Setting up WH handler")

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        print("Launching the Sending out email function")
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info
        print("Setting up the handle_payment_intent_succeeded function")

        billing_details = intent.charges.data[0].billing_details
        total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the billing details
        for field, value in billing_details.address.items():
            print(field)
            print(value)
            if value == "":
                billing_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            print("username not equal to anaon")
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = (
                    shipping_details.address.line1)
                profile.default_street_address2 = (
                    shipping_details.address.line2)
                profile.default_county = shipping_details.address.state
                profile.save()

        order_exists = False
        print("username is equal to anaon")
        print("trying to get the order")
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    first_name__iexact=billing_details.name.split(" ", 1),
                    last_name__iexact=billing_details.name.split(" ", 2),
                    email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                    country__iexact=billing_details.address.country,
                    postcode__iexact=billing_details.address.postal_code,
                    town_or_city__iexact=billing_details.address.city,
                    street_address1__iexact=billing_details.address.line1,
                    street_address2__iexact=billing_details.address.line2,
                    county__iexact=billing_details.address.state,
                    order_total=total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order_exists = True
                print("order exists")
                break
            except Order.DoesNotExist:
                print("order does exist")
                attempt += 1
                time.sleep(1)
        if order_exists:
            print("sending email becuase order exists")
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | \
                SUCCESS: Verified order already in database',
                status=200)
        else:
            print("order does not exist so trying to create it")
            order = None
            try:
                order = Order.objects.create(
                    first_name=billing_details.name.split(" ", 1),
                    last_name=billing_details.name.split(" ", 2),
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    country=billing_details.address.country,
                    postcode=billing_details.address.postal_code,
                    town_or_city=billing_details.address.city,
                    street_address1=billing_details.address.line1,
                    street_address2=billing_details.address.line2,
                    county=billing_details.address.state,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                for item_id, booking_details in json.loads(cart).items():
                    listing = Listing.objects.get(id=item_id)
                    selected_dates = booking_details['selected_dates']
                    for date in selected_dates:
                        order_line_item = OrderLineItem(
                            order=order,
                            listing=listing,
                            type='Reservation',
                            date=date,
                        )
                        order_line_item.save()
                    print("saved the order")
            except Exception as e:
                print("exception")
                if order:
                    order.delete()
                    print("order delete")
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        print("sending email bottom of function")
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | \
                SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
