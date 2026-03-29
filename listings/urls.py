from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('listings/',views.listings,name='listings'),
    path('listings/<slug:slug>/',views.property_detail, name='property_detail'),
]