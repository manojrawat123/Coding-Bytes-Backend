from django.db import models
from lead.models import Lead
from messagetemplate.models import SMSTemplate

class MessageSchedule(models.Model):
    ScheduleID = models.AutoField(primary_key=True)
    ScheduleDateTime = models.DateTimeField()
    ScheduleCustomers = models.ManyToManyField(Lead)  # Assuming you have a Customer model
    ScheduleTemplateID = models.ForeignKey(SMSTemplate, on_delete=models.CASCADE)  # Assuming you have a ScheduleTemplate model
    Status = models.CharField(max_length=20, choices=(
        ('active', 'Active'),
        ('not_active', 'Not Active'),
    ))

    def __str__(self):
        return f"Schedule {self.ScheduleID}"
