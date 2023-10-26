from django.db import models
from lead.models import Lead # Import the related models from your app
from emailtemplate.models import  EmailTemplate  # Import the related models from your app

class EmailSchedule(models.Model):
    ScheduleID = models.AutoField(primary_key=True)
    ScheduleDateTime = models.DateTimeField()
    ScheduleCustomers = models.ManyToManyField(Lead, related_name='scheduled_emails')
    ScheduleTemplate = models.ForeignKey(EmailTemplate, on_delete=models.CASCADE)

    def __str__(self):
        return f'Schedule {self.ScheduleID}'
