# account/forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core import validators
from django.contrib.auth.forms import AuthenticationForm

# Handmade
from mysite.account.models import UserModel


class UserLoginForm(AuthenticationForm):
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class':'uk-input fYekan gold-text border-radius-3','placeholder':''}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
'class':'uk-input fYekan gold-text input border-radius-3','placeholder':''
        }
))
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
