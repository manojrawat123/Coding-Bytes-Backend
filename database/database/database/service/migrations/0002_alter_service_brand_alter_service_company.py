# Generated by Django 4.0.3 on 2023-08-01 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('brand', '0001_initial'),
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='Brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brand.brand'),
        ),
        migrations.AlterField(
            model_name='service',
            name='Company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
    ]
