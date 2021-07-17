from django.urls import path
from . import views

urlpatterns = [
    path('', views.paidbills, name='paidbills'),
]