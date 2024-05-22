from django.urls import path
from . import views

# URL patterns for the users app
urlpatterns = [
    path('profile/', views.profile, name='profile'),  # URL pattern for the profile view
    # Add more URL patterns here as needed
]
