from django.forms import ModelForm

from .models import PrelaunchSignUp


class ContactUsForm(ModelForm):
    """
    Contact Us Form.
    """
    class Meta:
        model = PrelaunchSignUp
        fields = ['name', 'email']
