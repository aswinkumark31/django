from django import forms
from . models import *

class Application_Form(forms.ModelForm):
    class Meta:
        model=Enquiry
        fields='__all__'
