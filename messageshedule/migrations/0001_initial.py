# Generated by Django 4.0.3 on 2023-10-26 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('messagetemplate', '0001_initial'),
        ('lead', '0007_remove_lead_leadserviceinterested_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageSchedule',
            fields=[
                ('ScheduleID', models.AutoField(primary_key=True, serialize=False)),
                ('ScheduleDateTime', models.DateTimeField()),
                ('Status', models.CharField(choices=[('active', 'Active'), ('not_active', 'Not Active')], max_length=20)),
                ('ScheduleCustomers', models.ManyToManyField(to='lead.lead')),
                ('ScheduleTemplateID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messagetemplate.smstemplate')),
            ],
        ),
    ]
