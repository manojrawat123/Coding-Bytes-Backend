# Generated by Django 4.0.3 on 2024-01-12 06:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('leadfollowup', '0020_alter_leadfollowup_leadstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadfollowup',
            name='LeadStatusDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]