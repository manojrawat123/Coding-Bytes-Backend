from django.db import models
from emailtemplate.models import EmailTemplate
from lead.models import Lead

class EmailLog(models.Model):
    LogID = models.AutoField(primary_key=True)
    Date = models.DateField(auto_now_add=True)
    template_id = models.ForeignKey(EmailTemplate, on_delete=models.CASCADE)
    CompanyID = models.ManyToManyField(Lead)
    Attachment = models.FileField(upload_to='attachments/', null=True)

    def __str__(self):
        return f"Log {self.LogID}"
