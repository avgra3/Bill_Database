from django.shortcuts import render
from numpy import pi
import pandas as pd

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

# Models created
from .models import BillsPaid, Carriers

# Create your views here.
def paidbills(request):
    var1 = BillsPaid.objects.latest('search_q').search_query
    context = {'property': var1}
    return render(request, 'YOURVIEW', context)