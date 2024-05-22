from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    """
    Form for creating and updating blog posts.
    """
    class Meta:
        model = Post
        fields = ['title', 'content', 'published_date', 'image']  # Add more fields as needed
