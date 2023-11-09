# Generated by Django 4.0.3 on 2023-11-07 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leadfollowup', '0013_alter_leadfollowup_leadserviceinterested'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadfollowup',
            name='LeadStatus',
            field=models.CharField(choices=[('Fresh', 'Fresh'), ('Ready To Enroll', 'Ready To Enroll'), ('Visit scheduled', 'Visit scheduled'), ('Demo scheduled', 'Demo scheduled'), ('Highly Intersted', 'Highly Intersted'), ('Least Intersted', 'Least Intersted'), ('Distance Issue', 'Distance Issue'), ('Pricing Issue', 'Pricing Issue'), ('Already Taken Service', 'Already Taken Service'), ('Quality Issue', 'Quality Issue'), ('Not Interested Anymore', 'Not Interested Anymore'), ('Did Not Enquire', 'Did Not Enquire'), ('Only Wanted Information', 'Only Wanted Information'), ('Other', 'Other'), ('Try Next Time', 'Try Next Time')], max_length=2000, null=True),
        ),
    ]
