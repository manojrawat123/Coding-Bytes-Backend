# Generated by Django 4.0.3 on 2023-10-18 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0005_alter_lead_coursename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='LeadStatus',
            field=models.CharField(choices=[('Fresh', 'Fresh'), ('Ready To Enroll', 'Ready To Enroll'), ('Visit scheduled', 'Visit scheduled'), ('Demo scheduled', 'Demo scheduled'), ('Highly Intersted', 'Highly Intersted'), ('Least Intersted', 'Least Intersted'), ('Distance Issue', 'Distance Issue'), ('Pricing Issue', 'Pricing Issue'), ('Already Taken Service', 'Already Taken Service'), ('Quality Issue', 'Quality Issue'), ('Not Interested Anymore', 'Not Interested Anymore'), ('Did Not Enquire', 'Did Not Enquire'), ('Only Wanted Information', 'Only Wanted Information'), ('Other', 'Other')], max_length=50),
        ),
    ]