from django.test import TestCase, Client
# from django.shortcuts import reverse
from .forms import ReviewForm
from listings.models import Listing
from django.contrib.auth.models import User
from .models import Review
from profiles.models import UserProfile
from django.db import models
from django.contrib.auth import authenticate


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


class TestReviewViews(TestCase):

    # c = Client()

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

        # self.user.is_active = True
        # self.user.save()

        # Set password. Otherwise hash affects ability to log in.
        self.user.set_password('aComplexPassword11')
        self.user.save()

        # Find user_profile
        self.user_profile = UserProfile.objects.filter(user='9999')

        # logged_in = self.c.login(username='TestUser', password='aComplexPassword11')
        # print(logged_in)

    
    def test_redirects_if_not_logged_in_user(self):
        response = self.client.get('/reviews/')
        self.assertRedirects(response, '/accounts/login/?next=/reviews/')

    def test_gets_reviews_for_logged_in_user(self):
        self.client.login(username='TestUser', password='aComplexPassword11')
        response = self.client.get('/reviews/', follow=True)
        self.assertEqual(str(response.context['user']), 'TestUser')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/reviews.html')

    def test_get_user_reviews(self):
        self.review = Review.objects.create(
            user_profile=self.user_profile[0], listing=self.listing, rating='5', review_title="I am a great review", review="Review contents.")
        self.client.login(username='TestUser', password='aComplexPassword11')
        response = self.client.get('/reviews/', follow=True)
        self.assertContains(response, "I am a great review")
        self.assertContains(response, "By TestUser")
        self.assertContains(response, "5 / 5.0")
        self.assertContains(response, "Listing: test listing")
        self.assertContains(response, "Review contents.")

    # def test_add_review(self):

    # def test_edit_review(self):

    # def test_delete_review(self):

    # test have to be review owner for the above?
