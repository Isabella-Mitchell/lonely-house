from django.test import TestCase
from django.shortcuts import get_object_or_404
from .forms import ReviewForm
from listings.models import Listing
from django.contrib.auth.models import User
from .models import Review
from profiles.models import UserProfile
from django.db import models


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

    def test_rating_min_value_is_valid(self):
        form = ReviewForm({'rating': '-1', 'listing': self.listing})
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors.keys())
        self.assertEqual(form.errors['rating'][0], 'Ensure this value is greater than or equal to 0.')
        
    def test_rating_max_value_is_valid(self):
        form = ReviewForm({'rating': '6', 'listing': self.listing})
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors.keys())
        self.assertEqual(form.errors['rating'][0], 'Ensure this value is less than or equal to 5.')


class TestReviewModel(TestCase):

    def setUp(self):
        # setup before the tests
        # Create test listing
        self.listing = Listing.objects.create(
            name='test listing',
            price='20',
            no_sleeps='2',
            latitude='51.5007',
            longitude='0.1246',
            )
        # Create test user and save to create user profile
        self.user = User.objects.create(
            username='TestUser',
            password='mypassword1234',
            email='test@user.com',
            id='9999',
        )
        self.user.save()
        # Find user_profile
        self.user_profile = UserProfile.objects.filter(user='9999')

    def test_featured_defaults_to_false(self):
        review = Review.objects.create(
            user_profile=self.user_profile[0], listing=self.listing, rating='5')
        self.assertFalse(review.featured)

    # def test_foreignkey_cascade(self):
    #     self.review = Review.objects.create(
    #         user_profile=self.user_profile[0], listing=self.listing, rating='5')
    #     """
    #     Test all FKs have on_delete=models.CASCADE unless otherwise specified
    #     """
    #     for f in self.review._meta.get_fields():
    #         print(f)
    #         if isinstance(f, models.ForeignKey):
    #             print(models.ForeignKey)
    #             self.assertEquals(f.remote_field.on_delete, models.CASCADE, '{} failed, value was {}'.format(f.name, f.remote_field.on_delete))
    #             print(f.remote_field.on_delete)

    def test_foreignkey_cascade_delete(self):
        self.review = Review.objects.create(
            user_profile=self.user_profile[0], listing=self.listing, rating='5')
        f = self.review._meta.get_field('user_profile')
        self.assertEquals(f.remote_field.on_delete, models.CASCADE, '{} failed, value was {}'.format(f.name, f.remote_field.on_delete))
        f = self.review._meta.get_field('listing')
        self.assertEquals(f.remote_field.on_delete, models.CASCADE, '{} failed, value was {}'.format(f.name, f.remote_field.on_delete))


# class TestReviewViews(TestCase):