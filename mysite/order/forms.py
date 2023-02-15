# order/forms.py

from django import forms
from django.core import validators

from mysite.order.models import OrderModel


class OrderForm(forms.ModelForm):
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    class Meta():
        model = OrderModel
        fields = ('name','title','phone_number','description')
        widgets = {
            'name': forms.TextInput(attrs={'class':'uk-input fYekan redC-text border-radius-3','placeholder':''},),
            'phone_number': forms.TextInput(attrs={'class':'uk-input fYekan redC-text border-radius-3','placeholder':''},),
            'description': forms.Textarea(attrs={'style':'font-size:14px; ','class':'uk-textarea border-radius-3 fYekan input','rows':'10','placeholder':'هر گونه توضیحات دیگر را در صورت لزوم در این فیلد وارد نمائید.'},),
            'title': forms.TextInput(attrs={'class':'uk-input fYekan redC-text border-radius-3','placeholder':''},),
        }
