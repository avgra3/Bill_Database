from django.contrib import admin
from .models import Carrier, Product, Bill, BillPaid, MonthlyBreakdown

# Create a filter for paid bills
class ProfileBillPaid(admin.ModelAdmin):
    list_filter = ("paidBool", "paidDate")

# Registers models here so we can view them on the admin site.
admin.site.register(Carrier)
admin.site.register(Product)
admin.site.register(Bill)
admin.site.register(BillPaid, ProfileBillPaid)
admin.site.register(MonthlyBreakdown)
