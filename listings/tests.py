from django.test import TestCase
from .models import Listing, Category, Facility
from .constants import sleep_filters_constant


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


class TestFiltersAndSearch(TestCase):

    @classmethod
    def setUp(self):
        # setup before the tests

        self.category_true = Category.objects.create(
            name='test_category_true', friendly_name="Test Category True")

        self.category_false = Category.objects.create(
            name='test_category_false', friendly_name="Test Category False")

        self.facility_true = Facility.objects.create(
            name='test_facility_true', friendly_name='Test Facility True')

        self.facility_false = Facility.objects.create(
            name='test_facility_false', friendly_name='Test Facility False')
        
        self.listing_true = Listing.objects.create(
            name='Test Listing True',
            category=self.category_true,
            price='20',
            no_sleeps='2',
            latitude='51.5007',
            longitude='0.1246',
            )
        
        self.listing_false = Listing.objects.create(
            name='False Cottage',
            category=self.category_false,
            price='20',
            no_sleeps='6',
            latitude='51.5007',
            longitude='0.1246',
            )

        self.listing_true.facilities.add(self.facility_true)

        self.listing_false.facilities.add(self.facility_false)

    # need to make listing which matches these filters and check presence on page.

    def test_category_filter(self):
        # need to add a line where I'm actually applying this category?
        response = self.client.get('/listings/?category=test_category_true')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Listing True')
        self.assertNotContains(response, 'False Cottage')

    def test_sleeps_filter(self):
        response = self.client.get('/listings/?sleeps=2')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Listing True')
        self.assertNotContains(response, 'False Cottage')

    def test_facilities_filter(self):
        response = self.client.get('/listings/?facility=test_facility_true')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Listing True')
        self.assertNotContains(response, 'False Cottage')

    def test_search(self):
        response = self.client.get('/listings/?q=test+listing')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Listing True')
        self.assertNotContains(response, 'False Cottage')


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

    def test_category_string_method_returns_name(self):
        category = Category.objects.create(
            name='test_category', friendly_name="Test Category")
        self.assertEqual(str(category), 'test_category')
        self.assertEqual(category.get_friendly_name(), 'Test Category')

    def test_facility_string_method_returns_name(self):
        facility = Facility.objects.create(
            name='test_facility', friendly_name='Test Facility')
        self.assertEqual(str(facility), 'test_facility')
        self.assertEqual(facility.get_friendly_name(), 'Test Facility')

    # Add further tests for other models

