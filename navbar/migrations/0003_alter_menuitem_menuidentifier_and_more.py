# Generated by Django 4.0.3 on 2023-09-18 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navbar', '0002_alter_menuitem_menuidentifier_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='MenuIdentifier',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='UserRoles',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
