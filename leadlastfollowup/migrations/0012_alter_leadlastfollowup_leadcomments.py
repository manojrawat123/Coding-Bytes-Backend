# Generated by Django 4.0.3 on 2023-11-26 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leadlastfollowup', '0011_leadlastfollowup_leadcomments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadlastfollowup',
            name='LeadComments',
            field=models.TextField(),
        ),
    ]
