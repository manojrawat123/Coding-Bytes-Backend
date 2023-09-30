# Generated by Django 4.0.3 on 2023-08-30 07:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0001_initial'),
        ('paymenttype', '0001_initial'),
        ('lead', '0001_initial'),
        ('customerstudent', '0001_initial'),
        ('paymentmode', '0001_initial'),
        ('brand', '0001_initial'),
        ('payment', '0005_alter_payment_payment_type_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee_received', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fee_created_datetime', models.DateTimeField()),
                ('fee_payment_datetime', models.DateTimeField()),
                ('receipt_number', models.CharField(max_length=50)),
                ('customer_status', models.CharField(default='Active', max_length=100)),
                ('updated_by', models.CharField(max_length=100)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brand.brand')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('converted_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='converted_fees', to='lead.lead')),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lead.lead')),
                ('payment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.payment')),
                ('payment_mode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paymentmode.paymentmode')),
                ('payment_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paymenttype.paymenttype')),
                ('representative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fees', to='customerstudent.customer')),
            ],
        ),
    ]