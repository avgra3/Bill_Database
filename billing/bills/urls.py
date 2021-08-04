from django.urls import path
from . import views
from .views import (MonthlyBreakdownListView)

urlpatterns = [
    path('', views.homepage, name='pages/base.html'),
    #path('paidbills/', views.paidbills, name='paidbills')
    path('paidbills/', views.dashboard_with_pivot, name='dashboard_with_pivot'),
    path('paidbills/data/', views.pivot_data, name='pivot_data'),
    path('mb/', views.MonthlyBreakdownListView, name='bills-mb'),
]