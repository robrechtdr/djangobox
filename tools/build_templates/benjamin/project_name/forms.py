from django import forms
from .models import ModelBox

class ModelBoxForm(forms.ModelForm):
    class Meta:
        model = ModelBox

class CommentForm(forms.Form):
    comment = forms.CharField()
