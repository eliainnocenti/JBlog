from django.urls import path
from .views import homePageView # TODO: update

urlpatterns = [
    path('', homePageView, name='home')
]