# Generated by Django 4.0.3 on 2023-08-25 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payment', '0002_initial'),
        ('paymenttype', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paymenttype.paymenttype'),
        ),
    ]
