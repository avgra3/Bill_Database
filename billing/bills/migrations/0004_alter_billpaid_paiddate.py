# Generated by Django 3.2.5 on 2021-08-11 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0003_alter_billpaid_paidid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billpaid',
            name='paidDate',
            field=models.DateField(null=True, verbose_name='Date Paid'),
        ),
    ]