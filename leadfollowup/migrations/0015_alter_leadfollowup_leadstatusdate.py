# Generated by Django 4.0.3 on 2023-11-13 07:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('leadfollowup', '0014_alter_leadfollowup_leadstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadfollowup',
            name='LeadStatusDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
