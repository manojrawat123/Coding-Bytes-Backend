# Generated by Django 4.0.3 on 2023-12-01 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feetracer', '0003_alter_fee_converted_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='fee',
            name='next_due_date',
            field=models.DateField(default='2023-03-03'),
        ),
    ]
