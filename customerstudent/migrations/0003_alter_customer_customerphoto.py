# Generated by Django 4.0.3 on 2023-09-14 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerstudent', '0002_customer_customerphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='CustomerPhoto',
            field=models.ImageField(null=True, upload_to='ProfilePhoto'),
        ),
    ]
