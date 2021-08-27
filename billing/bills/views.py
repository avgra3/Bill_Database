from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import ListView
from django.db.models import Sum, Count, Avg, Q, Count, Case, When
from django.db.models.functions import TruncMonth
from numpy import pi
import pandas as pd

# Models created
from .models import BillPaid, Carrier, MonthlyBreakdown, Bill

# Homepage view.
def homepage(request):
    # Shows any unpaid bills:
    unpaid = BillPaid.objects.all().filter(paidBool=0).values('billID', 'totalPaid', 'notes')
    
    context = {"unpaid": unpaid}
    return render(request, 'pages/home.html', context=context)
    
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
def AverageBillPaidView(request):
    # Get the running average billed amount for all bills
    runningAvg = BillPaid.objects.aggregate(Ravg=Avg('totalPaid'))

    # We want to get the average cost for each carrier/utility
    monthlyAvg = BillPaid.objects.annotate(month=TruncMonth('paidDate')).values('month').annotate(a = Avg('totalPaid')).values('month', 'a').order_by('month')

    # Combines the two items we want to show in view
    context = {"runningAvg": runningAvg,  "monthlyAvg": monthlyAvg}

    return render(request = request, template_name='pages/bills-avg.html', context=context)



