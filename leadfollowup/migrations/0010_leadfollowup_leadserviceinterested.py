# Generated by Django 4.0.3 on 2023-10-18 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_alter_service_servicemode'),
        ('leadfollowup', '0009_alter_leadfollowup_leadstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='leadfollowup',
            name='LeadServiceInterested',
            field=models.ManyToManyField(to='service.service'),
        ),
    ]
