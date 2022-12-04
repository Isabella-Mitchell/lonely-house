from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews, name='reviews'),
]
