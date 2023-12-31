# Generated by Django 4.0.3 on 2023-10-03 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('convertedstudent', '0003_alter_convertedstudent_nextduedate'),
        ('lead', '0005_alter_lead_coursename'),
        ('batch', '0003_alter_batch_batchstaffassigned_and_more'),
        ('customerstudent', '0004_customer_customerdob_customer_customergender_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BatchStudent',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('BatchID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='batch.batch')),
                ('ConvertedID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='convertedstudent.convertedstudent')),
                ('CustomerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customerstudent.customer')),
                ('LeadId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lead.lead')),
            ],
        ),
    ]
