# Generated by Django 4.0.3 on 2023-08-31 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_alter_service_servicemode'),
        ('lead', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='LeadServiceInterested',
        ),
        migrations.AddField(
            model_name='lead',
            name='LeadServiceInterested',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='service.service'),
        ),
    ]
