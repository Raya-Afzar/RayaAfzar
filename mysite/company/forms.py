# company/forms.py

from django import forms
from django.core import validators

from mysite.company.models import ContactUsModel


class ContactUsForm(forms.ModelForm):
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    class Meta():
        model = ContactUsModel
        fields = ('name','email','phone_number','request')
        widgets = {
            'name': forms.TextInput(attrs={'class':'uk-input fYekan redC-text border-radius-3','placeholder':''},),
            'phone_number': forms.TextInput(attrs={'class':'uk-input fYekan border-radius-3','placeholder':''},),
            'request': forms.Textarea(attrs={'style':'font-size:14px; ','class':'border-radius-3 uk-textarea fYekan input','rows':'14','placeholder':'هر گونه انتقاد پیشنهاد یا درخواستی از ما دارید با ما در میان بگذارید'},),
            'email': forms.EmailInput(attrs={'class':'uk-input fYekan input border-radius-3','placeholder':''},),

        }
