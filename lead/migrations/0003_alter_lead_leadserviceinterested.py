# Generated by Django 4.0.3 on 2023-08-31 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_alter_service_servicemode'),
        ('lead', '0002_remove_lead_leadserviceinterested_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='LeadServiceInterested',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.service'),
        ),
    ]