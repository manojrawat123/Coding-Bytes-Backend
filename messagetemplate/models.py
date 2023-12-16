from django.db import models
from brand.models import Brand
from company.models import Company

class SMSTemplate(models.Model):
    TemplateID = models.AutoField(primary_key=True)
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE) 
    CompanyID = models.ForeignKey(Company, on_delete=models.CASCADE)
    TemplateName = models.CharField(max_length=255)  # Template Identifier
    TemplateMessage = models.TextField()
    Status = models.CharField(max_length=20, choices=(
        ('active', 'Active'),
        ('not_active', 'Not Active'),
    ))
    CreatedDateTime = models.DateTimeField(auto_now_add=True)
    SMSTemplateVariables = models.CharField(max_length=500)
    LastUpdatedDateTime = models.DateTimeField(auto_now=True)
    DLFID = models.PositiveBigIntegerField(default=1207161520341994378)
    def __str__(self):
        return self.TemplateName
    