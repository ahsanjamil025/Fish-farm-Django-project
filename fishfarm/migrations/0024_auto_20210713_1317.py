# Generated by Django 3.2.3 on 2021-07-13 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishfarm', '0023_auto_20210630_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='req_info',
            name='CustomerID',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='req_info',
            name='Postal_Address',
            field=models.CharField(max_length=500, null=True),
        ),
    ]