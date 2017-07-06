from unittest import TestCase
from django.test import RequestFactory
from django.urls import reverse

from coming_soon.views import ContactUsView


class ContactUsViewTest(TestCase):
    def setUp(self):
        self.user_data = {
            'name': 'John Doe',
            'email': 'fe@example.com'
        }
        self.factory = RequestFactory()

    def create_view_request(self):
        request = self.factory.get(reverse('coming-soon'))
        response = ContactUsView.as_view()(request)
        return response

    def test_coming_soon_get(self):
        response = self.create_view_request()
        self.assertEqual(response.status_code, 200)
        # TODO: Test get request.

    def test_send_email(self):
        response = self.create_view_request()
        self.assertEqual(response.status_code, 200)
        # TODO: Test sending of email.

    def test_create_user(self):
        response = self.create_view_request()
        self.assertEqual(response.status_code, 200)
        # TODO: Test create user.

    def test_post(self):
        response = self.create_view_request()
        self.assertEqual(response.status_code, 200)
        # TODO: Test post request.
