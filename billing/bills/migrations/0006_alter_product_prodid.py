# Generated by Django 3.2.5 on 2021-08-31 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0005_alter_billpaid_paiddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prodID',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]