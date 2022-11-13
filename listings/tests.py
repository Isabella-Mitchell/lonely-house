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

    # test that filter queries are not applied when page is loaded

    # test that filters load with page (e.g so user can apply filter)

    # test that user can apply filter (if request.GET:...)

# Test category by making a listing with a category, applying filter, seeing if that category is present, 
# also not applying that filter and seeing if not present e.g

# class TestFilters(TestCase):

#     def test_category_filter_wetlands(self):
#         listing = Listing.objects.create(
#             name='Test Wetlands Category', price='20.00', no_sleeps="2", category="wetlands")
#         response = self.client.get('/listings/?category=wetlands')


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

