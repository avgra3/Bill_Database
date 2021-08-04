from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import ListView
from django.db.models import Sum, Count
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
from .models import BillPaid, Carrier, MonthlyBreakdown

# Create your views here.
def homepage(request):
    return render(request, 'pages/base.html', {})

""" 
def paidbills(request):
    carrier_list = Carriers.objects.values('carrierName', 'carrierAcctNum')
    bills_paid_list = BillsPaid.objects.values('billID', 'totalPaid')

    df = pd.DataFrame(bills_paid_list).set_index('billID')
    dictionary = {
        "df": df.to_html()
    }    


    return render(request, 'pages/paidbills.html', context=dictionary)
 """
def pivot_data(request):
    dataset = BillPaid.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)
   

def dashboard_with_pivot(request):
    return render(request, 'pages/paidbills.html', {})


# Create a view that summarizes the bills table
def MonthlyBreakdownListView(request):
    context = MonthlyBreakdown.objects.annotate(month=TruncMonth('myPaid')).values('month').annotate(s = Sum('totalPaid')).values('month', 's').order_by('month')
    return render(request = request, template_name='pages/bills-mb.html', context={"mb": context})

