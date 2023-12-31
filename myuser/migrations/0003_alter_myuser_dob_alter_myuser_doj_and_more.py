# Generated by Django 4.0.3 on 2023-09-25 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0002_myuser_dob_myuser_doj_myuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='doj',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='user_type',
            field=models.CharField(choices=[('Caller', 'Caller'), ('View', 'View'), ('Admin', 'Admin'), ('Staff', 'Staff')], max_length=225),
        ),
    ]
