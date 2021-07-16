from django.contrib import admin
from .models import Carriers, Products, Bills, BillsPaid

# Register your models here.
admin.site.register(Carriers)
admin.site.register(Products)
admin.site.register(Bills)
admin.site.register(BillsPaid)