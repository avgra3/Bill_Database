from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import ListView
from django.db.models import Sum, Count, Avg, Q, Count, Case, When
from django.db.models.functions import TruncMonth
from numpy import pi
import pandas as pd

"""
# Specific to bokeh
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool, LassoSelectTool, WheelZoomTool, PointDrawTool, ColumnDataSource
from bokeh.palettes import Category20c, Spectral6
from bokeh.transform import cumsum
from bokeh.resources import CDN
"""

# Models created
from .models import BillPaid, Carrier, MonthlyBreakdown, Bill

# Homepage view.
def homepage(request):
    return render(request, 'pages/base.html', {})
    
# Pivoted data    
def pivot_data(request):
    dataset = BillPaid.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)
   

def dashboard_with_pivot(request):
    return render(request, 'pages/paidbills.html', {})


# Create a view that summarizes the bills table
def MonthlyBreakdownListView(request):
    # Will return a grouped breakdown for each month
    context = MonthlyBreakdown.objects.annotate(month=TruncMonth('myPaid')).values('month').annotate(s = Sum('totalPaid')).values('month', 's').order_by('month')

    
    return render(request = request, template_name='pages/bills-mb.html', context={"mb": context})

# Average bill view
def AvergaeBillView(request): 
    # Returns a dictionary with all carriers
    carrier_dict = Carrier.objects.all()

    # Returns a dictionary with all billID and carrierID
    bill_dict = Bill.objects.values('billID', 'carrierID')

    # We want to get the average cost for each carrier/utility
    context = BillPaid.objects.annotate(month=TruncMonth('paidDate')).values('month').annotate(a = Avg('totalPaid')).values('month', 'a').order_by('month')


    return render(request = request, template_name='pages/bills-avg.html', context={"avg": context})


# A view to show any unpaid bils which are in the database
def UnpaidBills(request):
    # Get the unpaid objects
    context = BillPaid.objects.all().filter(paidBool=0).values('billID', 'totalPaid', 'notes')

    return render(request = request, template_name='pages/base.html', context={"unpaid": context})


