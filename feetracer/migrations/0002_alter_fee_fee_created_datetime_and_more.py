# Generated by Django 4.0.3 on 2023-08-30 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feetracer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fee',
            name='fee_created_datetime',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='fee',
            name='fee_payment_datetime',
            field=models.DateField(),
        ),
    ]
