from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    """
    Form for creating and updating blog posts.
    """
    class Meta:
        model = Post
        fields = ['title', 'content', 'published_date', 'image']  # Add more fields as needed

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']