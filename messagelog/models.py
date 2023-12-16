from django.db import models
from messagetemplate.models import SMSTemplate  # Import the SMSTemplate model
from lead.models import Lead  # Import the Company model
from company.models import Company
from brand.models import Brand



class MessageLog(models.Model):
    LogID = models.AutoField(primary_key=True)
    Date = models.DateField(auto_now_add=True)
    TemplateID = models.ForeignKey(SMSTemplate, on_delete=models.CASCADE)
    CompanyID = models.ForeignKey(Company, on_delete=models.CASCADE)
    BrandId = models.ForeignKey(Brand, on_delete=models.CASCADE)
    MessageBody = models.TextField()
    LeadId = models.ForeignKey(Lead, on_delete=models.CASCADE)

    def __str__(self):
        return f"Message Log {self.LogID}"
