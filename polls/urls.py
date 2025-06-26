from django.urls import path
from . import views

urlpatterns = [
    path('address/', views.address_view, name='address'),
    path('phone/', views.phone_view, name='phone'),
]
