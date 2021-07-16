from django.db import models

# Create your models here.

# Creates the carriers table 
class Carriers(models.Model):
    carrierId = models.AutoField(primary_key=True)
    carrierName = models.CharField(max_length=40)
    carrierAcctNum = models.CharField(max_length=80)

    def __str__(self):
        return self.carrierName

# Creates the Products table
class Products(models.Model):
    prodID = models.AutoField(primary_key=True)
    product = models.CharField(max_length=80)

    def __str__(self):
        return self.product

# Creates the bills table
class Bills(models.Model):
    billID = models.AutoField(primary_key=True)
    carrierID = models.ForeignKey(Carriers, on_delete=models.CASCADE, verbose_name='related carrier')
    billDate = models.DateField(verbose_name='Billed Date')
    dueDate = models.DateField(verbose_name='Due Date')
    prodID = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='related product')
    charge = models.DecimalField(max_digits=65, decimal_places=2)
    anc_fees = models.DecimalField(max_digits=65, decimal_places=2, verbose_name='Ancilliary Fees')
    taxes = models.DecimalField(max_digits=65, decimal_places=2)
    credit = models.DecimalField(max_digits=65, decimal_places=2)

    def __str__(self):
        return self.billID


# Creates the Bills Paid table
class BillsPaid(models.Model):
    paidID = models.AutoField(primary_key=True)
    paidDate = models.DateField(verbose_name='Date Paid')
    billID = models.ForeignKey(Bills, on_delete=models.CASCADE, verbose_name='related bill')
    notes = models.CharField(max_length=100, default='N/A')
    paidBool = models.BooleanField(verbose_name='Paid (True or False)')
    totalPaid = models.DecimalField(max_digits=65, decimal_places=2, verbose_name='Total Paid')
    
    def __str__(self):
        return self.paidID

    

