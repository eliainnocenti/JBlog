from django.urls import path
from . import views
from .views import PostListView

# TODO: update the urls (these are temporary)

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('post/', views.post_list, name='post_list'),
]