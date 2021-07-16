from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
# Create your models here.

# Creates the carriers table 
class Carriers(models.Model):
    carrierId = models.IntegerField(primary_key=True, validators=[MinValueValidator(1), MaxValueValidator(10000)])
    carrierName = models.CharField(max_length=40)
    carrierAcctNum = models.CharField(max_length=80)

    def __str__(self):
        return f'{self.carrierName} - {self.carrierAcctNum}'

    class Meta:
        ordering = ['carrierName', 'carrierAcctNum']

# Creates the Products table
class Products(models.Model):
    prodID = models.IntegerField(primary_key=True, validators=[MinValueValidator(1), MaxValueValidator(10000)])
    product = models.CharField(max_length=80)

    def __str__(self):
        return self.product

    class Meta:
        ordering = ['product']

# Creates the bills table
class Bills(models.Model):
    billID = models.IntegerField(primary_key=True, validators=[MinValueValidator(1), MaxValueValidator(10000)])
    carrierID = models.ForeignKey(Carriers, on_delete=models.CASCADE, verbose_name='related carrier')
    billDate = models.DateField(verbose_name='Billed Date')
    dueDate = models.DateField(verbose_name='Due Date')
    prodID = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='related product')
    charge = models.DecimalField(max_digits=65, decimal_places=2)
    anc_fees = models.DecimalField(max_digits=65, decimal_places=2, verbose_name='Ancilliary Fees')
    taxes = models.DecimalField(max_digits=65, decimal_places=2)
    credit = models.DecimalField(max_digits=65, decimal_places=2)

    def dates(self):
        date = self.dueDate.strftime('%b %y')
        return date

    def __str__(self):
        date = self.dueDate.strftime('%b %y')
        return f'{self.carrierID} - {date}'

    class Meta:
        ordering = ['billDate']


# Creates the Bills Paid table
class BillsPaid(models.Model):
    def id_default():
        id = self.paidID.max()
        return id   

    paidID = models.IntegerField(primary_key=True, validators=[MinValueValidator(1), MaxValueValidator(10000)],
                                default=id_default)
    paidDate = models.DateField(verbose_name='Date Paid')
    billID = models.ForeignKey(Bills, on_delete=models.CASCADE, verbose_name='related bill')
    notes = models.CharField(max_length=100, default='N/A')
    paidBool = models.BooleanField(verbose_name='Paid (True or False)')
    totalPaid = models.DecimalField(max_digits=65, decimal_places=2, verbose_name='Total Paid')
    
    def __str__(self):
        return f'{self.paidID} - {self.billID}'

    class Meta:
        ordering = ['paidDate', 'billID']

    

    

