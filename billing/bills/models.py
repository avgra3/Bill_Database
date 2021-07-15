from django.db import models

# Create your models here.

# Creates the carriers table 
class Carriers(models.Model):
    carrierId = models.IntegerField(primary_key=True)
    carrierName = models.CharField(max_length=40)
    carrierAcctNum = models.CharField(max_length=80)

# Creates the Products table
class Products(models.Model):
    prodID = models.IntegerField(primary_key=True)
    product = models.CharField(max_length=80)

# Creates the bills table
class Bills(models.Model):
    billID = models.IntegerField(primary_key=True)
    carrierID = models.ForeignKey(Carriers, on_delete=models.CASCADE, verbose_name='related carrier')
    billDate = models.DateField()
    dueDate = models.DateField()
    prodID = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='related product')
    charge = models.DecimalField(max_digits=65, decimal_places=2)
    anc_fees = models.DecimalField(max_digits=65, decimal_places=2)
    taxes = models.DecimalField(max_digits=65, decimal_places=2)
    credit = models.DecimalField(max_digits=65, decimal_places=2)

# Creates the Bills Paid table
class BillsPaid(models.Model):
    paidID = models.IntegerField(primary_key=True)
    paidDate = models.DateField()
    billID = models.ForeignKey(Bills, on_delete=models.CASCADE, verbose_name='related bill')
    notes = models.CharField(max_length=100)
    paidBool = models.BooleanField()
    totalPaid = models.DecimalField(max_digits=65, decimal_places=2)

    

