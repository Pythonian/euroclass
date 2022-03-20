from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['full_name', 'pupil_class', 'image',
                  'date_of_birth', 'parent_name', 'contact_number',
                  'email', 'home_address']


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15)
    subject = forms.CharField(max_length=30, required=True)
    message = forms.TextField(required=True)
