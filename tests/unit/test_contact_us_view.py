from django.test import Client, TestCase
from django.urls import reverse, reverse_lazy
from django.core import mail
from django.conf import settings
from django.contrib.messages import get_messages

from coming_soon.forms import ContactUsForm


class ContactUsViewTest(TestCase):
    def setUp(self):
        self.user_data = {
            'name': 'John Doe',
            'email': 'jd@example.com'
        }
        self.client = Client()

    def create_view_get_request(self):
        return self.client.get(reverse_lazy('coming-soon'))

    def create_view_post_request(self, data=None):
        return self.client.post(reverse('coming-soon'), data=data)

    def test_coming_soon_get(self):
        response = self.create_view_get_request()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'contact.html')

    def test_coming_soon_post(self):
        response = self.create_view_post_request(data=self.user_data)
        self.assertEqual(response.status_code, 302)

        # Check that an email was sent to the user.
        self.assertEqual(len(mail.outbox), 1)

        # Check that an email was sent from the correct email account.
        self.assertEqual(mail.outbox[0].from_email, getattr(settings, 'PRELAUNCH_EMAIL', 'None'))

        # Check that an email was sent to the correct user.
        self.assertEqual(mail.outbox[0].to[0], self.user_data['email'])

        # Check that post redirects to same url.
        self.assertEqual(response.url, reverse('coming-soon'))

        messages = [m.message for m in get_messages(response.wsgi_request)]

        # Check success success message.
        self.assertIn('Your details were captured successfully.', messages)

    def test_coming_soon_post_form(self):
        invalid_form_data = {
            'name': '',
            'email': 'test'
        }
        form = ContactUsForm(data=invalid_form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'email': ['Enter a valid email address.'], 'name': ['This field is required.']})
        valid_form_data = {
            'name': 'John Doe',
            'email': 'cs@example.com'
        }
        form = ContactUsForm(data=valid_form_data)
        self.assertTrue(form.is_valid())