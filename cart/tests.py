from django.test import TestCase
from listings.models import Listing
# from django.contrib.auth import get_user_model
# from django.urls import reverse


class TestViews(TestCase):

    def test_view_cart(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')

    # def test_dates_to_string(self):

    # def test_add_to_cart(self):

    # def test_remove_from_cart(self):
