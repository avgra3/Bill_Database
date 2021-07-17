from django.urls import path
from . import views

urlpatterns = [
    path('bokeh/', views.home, name='home'),
    path('starter/', views.starter, name='starter'),
    path('leaning/', views.leaning, name='leaning'),
    path('combo/', views.combo, name='combo'),
    path('programming/', views.programming, name='programming'),
    path('multi_plot/', views.multi_plot, name='multi_plot'),
]