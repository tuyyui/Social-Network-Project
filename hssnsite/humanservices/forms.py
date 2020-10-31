from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import Snippet




class SnippetForm(forms.ModelForm):
    firstname = forms.CharField()
    lastname = forms.CharField()
    class Meta:
        model = Snippet
        fields = ['firstname', 'lastname']
