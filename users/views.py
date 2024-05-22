from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateForm, ProfileReadOnlyForm
from django.contrib.auth.decorators import login_required
import logging
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

logger = logging.getLogger(__name__)

def register(request):
    """
    Handle user registration. Display the registration form and save new user if form is valid.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for {username}. You can now log in!')
            logger.info(f'New user registered: {username}')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'users/login.html'

    def get_success_url(self):
        if self.request.user.is_staff:
            # Redirect admin users to the default admin site
            return reverse_lazy('admin:index')
        else:
            # Redirect regular users to their profile page
            return reverse_lazy('profile', kwargs={'username': self.request.user.username})

@login_required
def profile(request, username):
    """
    Display the profile of a user identified by the username. Requires login.
    """
    user = get_object_or_404(User, username=username)
    form = ProfileReadOnlyForm(instance=user.profile)
    return render(request, 'users/profile.html', {'user': user, 'form': form})

@login_required
def profile_update(request):
    """
    Handle profile updates for the logged-in user. Requires login.
    """
    user = request.user
    if request.method == 'POST':
        u_form = ProfileUpdateForm(request.POST, instance=user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            logger.info(f'Profile updated for user: {user.username}')
            return redirect('profile', username=user.username)
        else:
            messages.error(request, 'Update failed. Please correct the errors below.')
    else:
        u_form = ProfileUpdateForm(instance=user)
        p_form = ProfileUpdateForm(instance=user.profile)
    return render(request, 'users/profile_update.html', {'u_form': u_form, 'p_form': p_form})
