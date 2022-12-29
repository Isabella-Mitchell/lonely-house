from django.test import TestCase
from .models import Listing, Category


class TestViews(TestCase):

    def test_get_all_listings(self):
        response = self.client.get('/listings/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listings/listings.html')

    def test_get_listing_detail(self):
        listing = Listing.objects.create(
            name='Test Get Listing Details', price='20.00', no_sleeps="2", latitude=0.00, longitude=0.00)
        response = self.client.get(f'/listings/{listing.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listings/listing_detail.html')

    # add test for get_filters

    # add test for filters appearing on page


class TestFilters(TestCase):

    def test_category_filter_wetlands(self):
        category = Category.objects.create(
            name='test_wetlands_category', friendly_name="Test Wetlands Category")
        # need to add a line where I'm actually applying this category?
        response = self.client.get('/listings/?category=wetlands')
        self.assertEqual(response.status_code, 200)

    # Test category by making a listing with a category, applying filter, seeing if that category is present, 
    # also not applying that filter and seeing if not present


class TestModels(TestCase):

    def test_featured_defaults_to_false_category(self):
        category = Category.objects.create(
            name='test_category', friendly_name="Test Category")
        self.assertFalse(category.featured)

    def test_featured_defaults_to_false_listing(self):
        listing = Listing.objects.create(
            name='Test Get Listing Details', price='20.00', no_sleeps="2", latitude=0.00, longitude=0.00)
        self.assertFalse(listing.featured)

    def test_listing_string_method_returns_name(self):
        listing = Listing.objects.create(
            name='Test Get Listing Details', price='20.00', no_sleeps="2", latitude=0.00, longitude=0.00)
        self.assertEqual(str(listing), 'Test Get Listing Details')

    # Add further tests for other models

