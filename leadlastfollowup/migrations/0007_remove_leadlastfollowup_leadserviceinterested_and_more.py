# Generated by Django 4.0.3 on 2023-10-31 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_alter_service_servicemode'),
        ('leadlastfollowup', '0006_leadlastfollowup_leadserviceinterested'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leadlastfollowup',
            name='LeadServiceInterested',
        ),
        migrations.AddField(
            model_name='leadlastfollowup',
            name='LeadServiceInterested',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='service.service'),
        ),
    ]
