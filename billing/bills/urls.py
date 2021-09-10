from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='pages/home.html'),
    path('paidbills/', views.dashboard_with_pivot, name='dashboard_with_pivot'),
    path('paidbills/data/', views.pivot_data, name='pivot_data'),
    path('mb/', views.MonthlyBreakdownListView, name='bills-mb'),
    path('avg/', views.AverageBillPaidView, name='bills-avg'),
    path('graph/', views.GraphicalView, name='bills-graph'),
]