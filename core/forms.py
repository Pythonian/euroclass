from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date', 'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
        # self.fields['full_name'].widget.attrs.update(
        #     {'class': 'form-control',
        #      'placeholder': 'Surname, Firstname Middlename'})
        # self.fields['pupil_class'].widget.attrs.update(
        #     {'class': 'form-control'})
        # self.fields['image'].widget.attrs.update(
        #     {'class': 'form-control'})
        # self.fields['parent_name'].widget.attrs.update(
        #     {'class': 'form-control'})
        # self.fields['contact_number'].widget.attrs.update(
        #     {'class': 'form-control'})
        # self.fields['email'].widget.attrs.update(
        #     {'class': 'form-control'})
        # self.fields['home_address'].widget.attrs.update(
        #     {'class': 'form-control'})

    class Meta:
        model = Application
        exclude = ['created', 'updated']
        # fields = ['full_name', 'pupil_class', 'image',
        #           'date_of_birth', 'parent_name', 'contact_number',
        #           'email', 'home_address']


# class ContactForm(forms.ModelForm):
#     name = forms.CharField(max_length=30, required=True)
#     email = forms.EmailField(required=True)
#     phone = forms.CharField(max_length=15)
#     subject = forms.CharField(max_length=30, required=True)
#     message = forms.TextField(required=True)
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        # for field in self.visible_fields():
        #     field.field.widget.attrs['class'] = 'form-control'
