from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['created']  # Exclude non-editable fields from the form

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['updated']