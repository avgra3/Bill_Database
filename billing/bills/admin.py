from django.contrib import admin
from .models import Carriers, Products, Bills, BillsPaid

# Registers models here so we can view them on the admin site.
admin.site.register(Carriers)
admin.site.register(Products)
admin.site.register(Bills)
admin.site.register(BillsPaid)