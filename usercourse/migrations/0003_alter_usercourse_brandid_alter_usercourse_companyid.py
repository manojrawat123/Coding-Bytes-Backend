# Generated by Django 4.0.3 on 2023-11-09 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('brand', '0001_initial'),
        ('usercourse', '0002_usercourse_brandid_usercourse_companyid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercourse',
            name='BrandID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brand.brand'),
        ),
        migrations.AlterField(
            model_name='usercourse',
            name='CompanyID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
    ]
