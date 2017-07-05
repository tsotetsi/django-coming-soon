from .forms import ContactUsForm
from django.views.generic import FormView

from .models import PrelaunchSignUp


class ContactUsView(FormView):
    template_name = 'contact.html'
    form_class = ContactUsForm
    success_url = '/success/'

    def form_valid(self, form):
        return super(ContactUsView, self).form_valid(form)

    @staticmethod
    def create_user_details(name, email):
        PrelaunchSignUp.objects.create(name=name, email=email)

    def post(self, request, *args, **kwargs):
        data = request.POST
        name = data['name']
        email = data['email']

        self.create_user_details(name, email)
        return super(ContactUsView, self).post(request)
