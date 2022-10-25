from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_listings, name='listings'),
    path('<listing_id>', views.listing_detail, name='listing_detail'),
]
