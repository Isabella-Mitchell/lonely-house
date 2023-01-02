from django.test import TestCase, Client
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.models import User
from django.db import models


class TestUserProfileForm(TestCase):

    def test_user_is_excluded(self):
        form = UserProfileForm()
        self.assertEqual(form.Meta.exclude, ['user'])

    def test_fields_are_not_required(self):
        form = UserProfileForm({
            'default_phone_number': '',
            'default_street_address1': '',
            'default_street_address2': '',
            'default_town_or_city': '',
            'default_county': '',
            'default_postcode': '',
        })
        self.assertTrue(form.is_valid())

    def test_form_item_input_has_placeholders(self):
        form = UserProfileForm()
        self.assertIn('placeholder="Phone Number"', form.as_p())
        self.assertIn('placeholder="Street Address 1"', form.as_p())
        self.assertIn('placeholder="Street Address 2"', form.as_p())
        self.assertIn('placeholder="Town or City"', form.as_p())
        self.assertIn('placeholder="County"', form.as_p())
        self.assertIn('placeholder="Postal Code"', form.as_p())


class TestUserProfileModel(TestCase):

    @classmethod
    def setUp(self):
        # Create test user
        self.user = User.objects.create(
            username='TestUser',
            password='mypassword1234',
            email='test@user.com',
            id='9999',
        )

        self.user.save()
        self.user_profiles = UserProfile.objects.all()
        self.entry = self.user_profiles[0]

    # duplicate of string method test
    # def test_create_user_profile_on_save(self):
    #     user_profile = UserProfile.objects.filter(user='9999')
    #     self.assertEqual(str(user_profile[0]), 'TestUser')

    # duplicate of view?
    # def test_update_user_profile_on_save(self):
    #     user_profiles = UserProfile.objects.all()
    #     entry = user_profiles[0]
    #     self.assertEqual(entry.default_phone_number, None)

    def test_string_method_returns_username(self):
        self.assertEqual(str(self.entry), 'TestUser')

    # def test_string_method_returns_username(self):
    #     self.user.save()
    #     self.user_profile = UserProfile.objects.filter(user='9999')
    #     self.assertEqual(str(self.user_profile), 'TestUser')

    def test_foreignkey_cascade_delete(self):
        f = self.entry._meta.get_field('user')
        self.assertEquals(
            f.remote_field.on_delete, models.CASCADE,
            '{} failed, value was {}'.format(f.name, f.remote_field.on_delete))


class TestUserProfileViews(TestCase):

    @classmethod
    def setUp(self):
        # Create test user
        self.user = User.objects.create(
            username='TestUser',
            password='mypassword1234',
            email='test@user.com',
            id='9999',
        )

        self.user.save()

        # Set password. Otherwise hash affects ability to log in.
        self.user.set_password('aComplexPassword11')
        self.user.save()

        # Find user_profile
        self.user_profile = UserProfile.objects.filter(user='9999')

    def test_redirects_from_profile_if_not_logged_in_user(self):
        response = self.client.get('/profile/')
        self.assertRedirects(response, '/accounts/login/?next=/profile/')

    def test_displays_profile_for_logged_in_user(self):
        self.client.login(username='TestUser', password='aComplexPassword11')
        response = self.client.get('/profile/', follow=True)
        self.assertEqual(str(response.context['user']), 'TestUser')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_user_can_update_profile_with_success_message(self):
        self.client.login(username='TestUser', password='aComplexPassword11')
        response = self.client.get('/profile/', follow=True)
        # self.assertEqual(len(response.context['key']), 0)
        user = self.user_profile[0]
        self.assertEqual(user.default_phone_number, None)
        self.assertEqual(user.default_street_address1, None)
        self.assertEqual(user.default_street_address2, None)
        self.assertEqual(user.default_town_or_city, None)
        self.assertEqual(user.default_county, None)
        self.assertEqual(user.default_postcode, None)
        response = self.client.post('/profile/', {
            'default_phone_number': '0123456789',
            'default_street_address1': 'Test Line 1',
            'default_street_address2': 'Test Line 2',
            'default_town_or_city': 'Test Ville',
            'default_county': 'Testshire',
            'default_postcode': 'TEST ING',
        })
        # Shows success message to user
        self.assertContains(response, 'Profile updated successfully')
        # Updated user profile is displayed to user
        response = self.client.get('/profile/', follow=True)
        self.assertContains(response, '0123456789')
        self.assertContains(response, 'Test Line 1')
        self.assertContains(response, 'Test Line 2')
        self.assertContains(response, 'Test Ville')
        self.assertContains(response, 'Testshire')
        self.assertContains(response, 'TEST ING')

    def test_error_message_shown_when_form_is_not_valid(self):
        self.client.login(username='TestUser', password='aComplexPassword11')
        response = self.client.post('/profile/', {
            'default_phone_number': 44444444444444444444444444,
        })
        self.assertContains(
            response, 'Update failed. Please ensure the form is valid.')
        self.assertIn('form', response.context)
        form = response.context['form']
        self.assertTrue(form.errors)
        self.assertIn('default_phone_number', form.errors.keys())

# tests for order history
