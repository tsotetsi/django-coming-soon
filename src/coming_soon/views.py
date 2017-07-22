from django.views.generic import FormView
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactUsForm
from .models import PrelaunchSignUp


class ContactUsView(FormView):
    template_name = 'contact.html'
    form_class = ContactUsForm
    success_url = '/coming-soon/'  # TODO: use reverse('coming-soon')

    @staticmethod
    def send_email(to_email):
        send_mail(
            subject='Thank you for contacting us!',
            message='Thank you for contacting us. You will be notified once the product goes live.',
            from_email=getattr(settings, 'PRELAUNCH_EMAIL', 'None'),
            recipient_list=[to_email]
        )

    @staticmethod
    def create_user(user_data):
        PrelaunchSignUp.objects.create(name=user_data['name'], email=user_data['email'])

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            user_data = request.POST
            self.create_user(user_data)
            self.send_email(to_email=user_data['email'])
            messages.success(request, 'Your details were captured successfully.')
        return super(ContactUsView, self).post(request)
