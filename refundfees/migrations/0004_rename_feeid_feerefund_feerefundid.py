# Generated by Django 4.0.3 on 2023-12-14 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('refundfees', '0003_alter_feerefund_feerefundedcreateddatetime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feerefund',
            old_name='FeeID',
            new_name='FeeRefundID',
        ),
    ]