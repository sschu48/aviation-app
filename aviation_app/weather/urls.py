from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='weather-home'),
    path('taf/', views.taf, name='weather-taf'),
    path('metar/', views.metar, name='weather-metar'),
]