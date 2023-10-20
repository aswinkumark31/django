from django import forms
from . models import *

class Batch_filter(forms.Form):
    batch=forms.ModelChoiceField(queryset=Batch.objects.all())