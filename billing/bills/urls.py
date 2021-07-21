from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='pages/base.html'),
    path('paidbills/', views.paidbills, name='paidbills')
]