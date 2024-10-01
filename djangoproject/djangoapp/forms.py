from django import forms
from django.db.models import CharField
from django.template.context_processors import request

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)
