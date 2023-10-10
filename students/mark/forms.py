from django import forms
from . import models


class Mark_upload(forms.ModelForm):
    class Meta:
        model=models.Mark
        fields='__all__'

