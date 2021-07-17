from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('starter/', views.starter, name='starter'),
    path('leaning/', views.leaning, name='leaning'),
]