from django.test import TestCase
from listings.models import Listing
from .utils import dates_string_to_list
from django.urls import reverse


class TestViews(TestCase):

    @classmethod
    def setUp(self):
        # setup before the tests
        self.listing = Listing.objects.create(
            name='test listing',
            price='20',
            no_sleeps='2',
            latitude='51.5007',
            longitude='0.1246',
            )

    def test_view_cart(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')

    def test_cart_is_empty(self):
        response = self.client.get('/cart/')
        self.assertEqual(len(response.context['cart_items']), 0)

    def test_add_to_cart(self):
        response = self.client.post(
            '/cart/add/'+str(self.listing.id)+'/', data={
                'selected-no-nights-input': '2',
                'selected-dates-array-input': '2023-11-22,2023-11-23,2023-11-24',
                'startDate': '2023-11-22',
                'endDate': '2023-11-24',
            })
        response = self.client.get('/cart/')
        self.assertContains(response, "test listing")
        self.assertEqual(len(response.context['cart_items']), 1)

    def test_remove_from_cart(self):
        response = self.client.post(
            '/cart/add/'+str(self.listing.id)+'/', data={
                'selected-no-nights-input': '2',
                'selected-dates-array-input': '2023-11-22,2023-11-23,2023-11-24',
                'startDate': '2023-11-22',
                'endDate': '2023-11-24',
            })
        response = self.client.get('/cart/')
        self.assertEqual(len(response.context['cart_items']), 1)
        response = self.client.post(
            '/cart/remove/'+str(self.listing.id)+'/')
        response = self.client.get('/cart/')
        self.assertEqual(len(response.context['cart_items']), 0)


class TestUtils(TestCase):

    def test_dates_to_string(self):
        self.assertEqual(
            dates_string_to_list(
                "23-11-22,23-11-23"), ['23-11-22'])
        self.assertEqual(
            dates_string_to_list(
                "23-11-22,23-11-23,23-11-34"), ['23-11-22', '23-11-23'])
