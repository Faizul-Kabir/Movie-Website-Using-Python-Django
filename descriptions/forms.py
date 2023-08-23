from django import forms
from . import models

class AddMovie(forms.ModelForm):
    class Meta:
        model=models.Description
        fields=['title','body','image']

    