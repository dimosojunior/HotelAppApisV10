# Generated by Django 4.2.6 on 2023-10-11 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApis', '0003_myuser_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelcustomers',
            name='CustomerEmail',
            field=models.EmailField(blank=True, max_length=200, null=True, verbose_name='Customer Email'),
        ),
    ]
