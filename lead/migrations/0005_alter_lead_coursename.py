# Generated by Django 4.0.3 on 2023-09-02 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0004_lead_coursename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='CourseName',
            field=models.CharField(max_length=300),
        ),
    ]
