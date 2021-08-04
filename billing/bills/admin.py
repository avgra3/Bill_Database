from django.contrib import admin
from .models import Carrier, Product, Bill, BillPaid, MonthlyBreakdown

# Registers models here so we can view them on the admin site.
admin.site.register(Carrier)
admin.site.register(Product)
admin.site.register(Bill)
admin.site.register(BillPaid)
admin.site.register(MonthlyBreakdown)