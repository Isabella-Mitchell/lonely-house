from django.test import TestCase
from .models import Listing


class TestViews(TestCase):

    def test_get_all_listings(self):
        response = self.client.get('/listings/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listings/listings.html')

    def test_get_listing_detail(self):
        listing = Listing.objects.create(
            name='Test Get Listing Details', price='20.00', no_sleeps="2")
        response = self.client.get(f'/listings/{listing.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listings/listing_detail.html')

    # test search & filters

    # test context in views?


# test form (for filters)


class TestModels(TestCase):

    def test_featured_defaults_to_false(self):
        listing = Listing.objects.create(
            name='Test Get Listing Details', price='20.00', no_sleeps="2")
        self.assertFalse(listing.featured)

    def test_listing_string_method_returns_name(self):
        listing = Listing.objects.create(
            name='Test Get Listing Details', price='20.00', no_sleeps="2")
        self.assertEqual(str(listing), 'Test Get Listing Details')

    # Add further tests for other models


