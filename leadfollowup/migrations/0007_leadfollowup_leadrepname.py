# Generated by Django 4.0.3 on 2023-09-01 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leadfollowup', '0006_alter_leadfollowup_leadstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='leadfollowup',
            name='leadRepName',
            field=models.CharField(default='Manoj Rawat', max_length=200),
        ),
    ]
