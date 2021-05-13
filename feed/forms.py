from django import forms

from .models import Post

class PostForm(forms.Form):
    text = forms.CharField()
    image = forms.FileField()


