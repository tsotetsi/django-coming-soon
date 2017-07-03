from .forms import ContactUsForm
from django.views.generic import FormView


class ContactUsView(FormView):
    template_name = 'contact.html'
    form_class = ContactUsForm
    success_url = '/success/'

    def form_valid(self, form):
        return super(ContactUsView, self).form_valid(form)
