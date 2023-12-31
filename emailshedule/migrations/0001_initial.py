# Generated by Django 4.0.3 on 2023-10-18 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lead', '0006_alter_lead_leadstatus'),
        ('emailtemplate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSchedule',
            fields=[
                ('ScheduleID', models.AutoField(primary_key=True, serialize=False)),
                ('ScheduleDateTime', models.DateTimeField()),
                ('ScheduleCustomers', models.ManyToManyField(related_name='scheduled_emails', to='lead.lead')),
                ('ScheduleTemplate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emailtemplate.emailtemplate')),
            ],
        ),
    ]
