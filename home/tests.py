from django.test import TestCase


class TestViews(TestCase):

    def test_load_homepage_view(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
