# Generated by Django 4.0.3 on 2023-09-21 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refundfees', '0002_alter_feerefund_receiptnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feerefund',
            name='FeeRefundedCreatedDateTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]