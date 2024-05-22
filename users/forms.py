from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    """
    Form for user registration.
    """
    email = forms.EmailField(help_text='Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        """
        Validate username uniqueness.
        """
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already taken.')
        return username

    def clean_email(self):
        """
        Validate email uniqueness.
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered.')
        return email


class ProfileUpdateForm(forms.ModelForm):
    """
    Form for updating user profile.
    """
    email = forms.EmailField(help_text='Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileReadOnlyForm(forms.ModelForm):
    """
    Read-only form for displaying user profile image.
    """
    class Meta:
        model = Profile
        fields = ['image']
