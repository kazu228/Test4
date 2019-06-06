from django import forms
from .models import Post

class HelloForm(forms.Form):

    name = forms.CharField(label='name')
    title = forms.CharField(label='title')
    text = forms.CharField(label='text', max_length=1000, widget=forms.Textarea)
    # file = forms.FileField(required=False)
    