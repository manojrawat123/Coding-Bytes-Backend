# Generated by Django 4.0.3 on 2023-08-01 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ServiceName', models.CharField(max_length=100)),
                ('ServiceType', models.CharField(max_length=50)),
                ('ServiceWebDisplay', models.URLField(blank=True, null=True)),
                ('Brand', models.CharField(max_length=50)),
                ('Company', models.CharField(max_length=100)),
                ('ServiceStatus', models.CharField(max_length=20)),
            ],
        ),
    ]
