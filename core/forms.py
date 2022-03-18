from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['full_name', 'pupil_class', 'image',
                  'date_of_birth', 'parent_name', 'contact_number',
                  'email', 'home_address']
