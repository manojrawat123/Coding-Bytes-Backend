# Generated by Django 4.0.3 on 2024-01-16 06:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feetracer', '0004_fee_next_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fee',
            name='fee_created_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]