from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import ListView
from django.db.models import Sum, Count, Avg, Q, Count, Case, When, F
from django.db.models.functions import TruncMonth
from numpy import pi
import pandas as pd

# Matplotlib utilities functions
from .utils import mb_bar

# Models created
from .models import BillPaid, Carrier, MonthlyBreakdown, Bill

# Homepage view.
def homepage(request):
    # Shows any unpaid bills:
    unpaid = BillPaid.objects.all().filter(paidBool=0).values('billID', 'totalPaid', 'notes')
    
    # Show previous 5 bills
    paid = BillPaid.objects.all().select_related('billID').order_by('-paidDate')[:5]

    context = {"unpaid": unpaid, "paid":paid}
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

# Creating a graphical views
def GraphicalView(request):
    mb = MonthlyBreakdown.objects.annotate(month=TruncMonth('myPaid')).values('month').annotate(s = Sum('totalPaid')).values('month', 's').order_by('month')

    # Combined
    bills = Bill.objects.select_related('carrierID').values('carrierID').annotate(col_sum=F('charge')+F('anc_fees')+F('taxes')+F('credit')).annotate(total = Sum('col_sum')).values('carrierID_id', 'total').order_by()

    # Context for carrier ID
    carriers = Carrier.objects.all()

    context = {"mb": mb, "bills": bills}

    return render(request, 'pages/bills-graph.html', context = context)


