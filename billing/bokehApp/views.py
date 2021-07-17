from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    first_graph = 'Success'
    return HttpResponse(first_graph)