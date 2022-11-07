from django.test import TestCase
from .models import Listing


class TestViews(TestCase):

    def test_get_all_listings(self):
        response = self.client.get('/listings/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listings/listings.html')

    def test_get_listing_detail(self):
        item = Listing.objects.create(
            name='Test Get Listing Details', price='20.00', no_sleeps="2")
        response = self.client.get(f'/listings/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listings/listing_detail.html')

    # test search & filters

    # test context?

# test form (for filters)
