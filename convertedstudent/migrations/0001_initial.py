# Generated by Django 4.0.3 on 2023-08-30 04:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lead', '0001_initial'),
        ('brand', '0001_initial'),
        ('payment', '0005_alter_payment_payment_type_id'),
        ('company', '0001_initial'),
        ('customerstudent', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='convertedstudent',
            fields=[
                ('ConvertedID', models.AutoField(primary_key=True, serialize=False)),
                ('CourseName', models.CharField(max_length=255)),
                ('ClassMode', models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline')], max_length=2000)),
                ('CreatedDateTime', models.DateTimeField(auto_now_add=True)),
                ('ConvertedDateTime', models.DateTimeField(auto_now_add=True)),
                ('CourseStartDate', models.DateField()),
                ('CourseEndDate', models.DateField()),
                ('CourseExpiryDate', models.DateField(blank=True, null=True)),
                ('TotalFee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('NextDue', models.DecimalField(decimal_places=2, max_digits=10)),
                ('UpdateBY', models.CharField(max_length=100)),
                ('CustomerStatus', models.CharField(default='Active', max_length=20)),
                ('LostSales', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('LostSalesDate', models.DateField(blank=True, null=True)),
                ('LostSalesReason', models.TextField(blank=True, null=True)),
                ('SecureKey', models.CharField(blank=True, max_length=100, null=True)),
                ('Brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brand.brand')),
                ('Company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('LeadID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lead.lead')),
                ('PaymentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.payment')),
                ('Representative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('StudentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customerstudent.customer')),
            ],
        ),
    ]
