from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # Specify the fields you want in the form

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
