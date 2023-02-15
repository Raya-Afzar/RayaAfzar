# project/forms.py

from django import forms
from django.core import validators

from mysite.project.models import ProjectModel


class ProjectForm(forms.ModelForm):

    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta():

        model = ProjectModel
        fields = ('name','client','url','description','production_date','program_type',
            'picture_1', 'picture_2', 'picture_3', 'picture_4', 'picture_5', 'picture_6',
            'picture_7', 'picture_8', 'picture_9', )
        widgets = {
            'name': forms.TextInput(attrs={},),
            'client': forms.TextInput(attrs={},),
            'description': forms.Textarea(attrs={},),
            'production_date': forms.DateInput(attrs={},),
            'url': forms.URLInput(attrs={},),
        }
