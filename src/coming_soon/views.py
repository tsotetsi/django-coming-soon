from django.views.generic import FormView
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.urls import reverse_lazy

from .forms import ContactUsForm
from .models import PrelaunchSignUp


class ContactUsView(FormView):
    template_name = 'contact.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('coming-soon')

    @staticmethod
    def send_user_email(user_email):
        msg = EmailMessage(
            subject='Thank you for contacting us!',
            body='Thank you for contacting us You will be notified once the product goes live.',
            from_email=getattr(settings, 'PRELAUNCH_EMAIL', 'None'),
            to=[user_email, ]
        )
        msg.send()

    @staticmethod
    def create_user(user_data):
        PrelaunchSignUp.objects.create(name=user_data['name'], email=user_data['email'])

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            user_data = request.POST
            self.create_user(user_data)
            self.send_user_email(user_email=user_data['email'])
            messages.success(request, 'Your details were captured successfully.')
        return super(ContactUsView, self).post(request)
