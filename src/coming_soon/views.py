from django.views.generic import FormView
from django.contrib import messages

from .forms import ContactUsForm
from .models import PrelaunchSignUp


class ContactUsView(FormView):
    template_name = 'contact.html'
    form_class = ContactUsForm
    success_url = '/coming-soon/'  # TODO: use reverse('coming-soon')

    def form_valid(self, form):
        return super(ContactUsView, self).form_valid(form)

    @staticmethod
    def create_user(user_data):
        PrelaunchSignUp.objects.create(name=user_data['name'], email=user_data['email'])

    def post(self, request, *args, **kwargs):
        user_data = request.POST

        self.create_user(user_data)
        messages.success(request, 'Your details were captured successfully.')
        return super(ContactUsView, self).post(request)
