# Generated by Django 4.0.3 on 2023-08-25 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMode',
            fields=[
                ('payment_mode_id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_mode', models.CharField(choices=[('PayTM', 'PayTM'), ('Swipe Machine', 'Swipe Machine'), ('Cash', 'Cash'), ('Bank Transfer', 'Bank Transfer')], max_length=1000)),
                ('payment_mode_display', models.CharField(max_length=100)),
                ('payment_mode_status', models.BooleanField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brand.brand')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
            options={
                'unique_together': {('brand', 'payment_mode')},
            },
        ),
    ]