from django.test import TestCase
from django.urls import reverse
from listings.models import Listing


class TestCheckout(TestCase):

    def setUp(self):
        # setup before the tests
        self.listing = Listing.objects.create(
            name='test listing',
            price='20',
            no_sleeps='2',
            latitude='51.5007',
            longitude='0.1246',
            )

    def test_view_checkout_nothing_in_cart(self):
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 302)

    def test_view_checkout_with_cart(self):
        response = self.client.post(
            '/cart/add/'+str(self.listing.id)+'/', data={
                'selected-no-nights-input': '2',
                'selected-dates-array-input': '2023-11-22,2023-11-23,2023-11-24',
                'startDate': '2023-11-22',
                'endDate': '2023-11-24',
            })
        response = self.client.get('/checkout/')
        self.assertTemplateUsed(response, "checkout/checkout.html")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test listing")