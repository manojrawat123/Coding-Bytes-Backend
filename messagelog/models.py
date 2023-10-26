from django.db import models
from messagetemplate.models import SMSTemplate  # Import the SMSTemplate model
from lead.models import Lead  # Import the Company model

class MessageLog(models.Model):
    LogID = models.AutoField(primary_key=True)
    Date = models.DateField()
    TemplateID = models.ForeignKey(SMSTemplate, on_delete=models.CASCADE)
    CompanyID = models.ManyToManyField(Lead)
    Attachment = models.FileField(upload_to='attachments/', null=True)

    def __str__(self):
        return f"Message Log {self.LogID}"
