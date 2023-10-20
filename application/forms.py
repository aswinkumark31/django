from django import forms
from . models import *

class Todo_form(forms.ModelForm):
    class Meta:
        model=Todo
        fields='__all__'