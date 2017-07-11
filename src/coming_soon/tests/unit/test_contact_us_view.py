from unittest import TestCase

from django.test import RequestFactory
from django.urls import reverse
from django.contrib.messages.storage.fallback import FallbackStorage
from django.core import mail

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

    def create_view_post_request(self):
        request = self.factory.post(reverse('coming-soon'), data=self.user_data)
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        response = ContactUsView.as_view()(request)
        return response

    def test_coming_soon_get(self):
        response = self.create_view_request()
        self.assertEqual(response.status_code, 200)

    def test_coming_soon_post(self):
        response = self.create_view_post_request()
        self.assertEqual(response.status_code, 200)

    def test_send_email(self):
        response = self.create_view_post_request()
        import pdb;pdb.set_trace()

    def test_create_user(self):
        response = self.create_view_request()
        self.assertEqual(response.status_code, 200)
        # TODO: Test create user.

    def test_post(self):
        response = self.create_view_request()
        self.assertEqual(response.status_code, 200)
        # TODO: Test post request.
