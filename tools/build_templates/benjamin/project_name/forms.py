from django.forms import Form, ModelForm
from models import Search

class BoxModelForm(ModelForm):
    class Meta:
        model = BoxModel

class CommentForm(forms.Form):
    comment = forms.CharField()
