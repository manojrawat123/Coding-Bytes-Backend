# Generated by Django 4.0.3 on 2023-12-12 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messagelog', '0004_messagelog_messagebody'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagelog',
            name='MessageBody',
            field=models.TextField(),
        ),
    ]