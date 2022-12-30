from django.test import TestCase
from .forms import ReviewForm
from listings.models import Listing


class TestReviewForm(TestCase):

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

    def test_rating_is_required(self):
        form = ReviewForm({'rating': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors.keys())
        self.assertEqual(form.errors['rating'][0], 'This field is required.')

    def test_listing_is_required(self):
        form = ReviewForm({'listing': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('listing', form.errors.keys())
        self.assertEqual(form.errors['listing'][0], 'This field is required.')

    def test_review_is_not_required(self):
        form = ReviewForm({'rating': '5', 'listing': self.listing})
        self.assertTrue(form.is_valid())

    def test_excluded_fields_are_hidden(self):
        form = ReviewForm()
        self.assertEqual(form.Meta.exclude, ['user_profile', 'featured'])
