# Generated by Django 4.0.3 on 2023-08-08 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_service_servicemode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='serviceMode',
            field=models.CharField(choices=[('online', 'Online'), ('offline', 'Offline')], max_length=10),
        ),
    ]
