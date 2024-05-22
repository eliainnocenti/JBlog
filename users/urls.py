from django.urls import path
from . import views
from .views import CustomLoginView

# URL patterns for the users app
urlpatterns = [
    path('profile/<str:username>/', views.profile, name='profile'),         # URL pattern for the profile view
    path('profile/update/', views.profile_update, name='profile_update'),   # URL pattern for the profile update view
    path('register/', views.register, name='register'),                     # URL pattern for user registration
    path('login/', CustomLoginView.as_view(), name='login'),                # URL pattern for user login
    # Add more URL patterns here as needed
]
