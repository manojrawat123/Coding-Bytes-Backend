# Generated by Django 4.0.3 on 2023-11-14 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_remove_payment_payment_mode_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_type',
            field=models.CharField(default='Registration', max_length=1000),
        ),
    ]