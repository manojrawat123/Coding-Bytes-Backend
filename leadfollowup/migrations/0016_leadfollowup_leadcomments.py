# Generated by Django 4.0.3 on 2023-11-26 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leadfollowup', '0015_alter_leadfollowup_leadstatusdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='leadfollowup',
            name='LeadComments',
            field=models.TextField(default='Dummy Comments'),
        ),
    ]