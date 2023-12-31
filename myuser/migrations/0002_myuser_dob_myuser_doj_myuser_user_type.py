# Generated by Django 4.0.3 on 2023-09-25 09:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='dob',
            field=models.DateField(default=datetime.date(2020, 3, 5)),
        ),
        migrations.AddField(
            model_name='myuser',
            name='doj',
            field=models.DateField(default=datetime.date(2020, 3, 5)),
        ),
        migrations.AddField(
            model_name='myuser',
            name='user_type',
            field=models.CharField(choices=[('Caller', 'Caller'), ('View', 'View'), ('Admin', 'Admin'), ('Staff', 'Staff')], default='Caller', max_length=225),
        ),
    ]
