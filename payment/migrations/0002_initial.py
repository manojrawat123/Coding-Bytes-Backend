# Generated by Django 4.0.3 on 2023-08-25 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paymentmode', '0001_initial'),
        ('payment', '0001_initial'),
        ('service', '0005_alter_service_servicemode'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_mode_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paymentmode.paymentmode'),
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_purpose',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.service'),
        ),
    ]
