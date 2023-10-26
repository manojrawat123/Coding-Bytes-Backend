from django.db import models

class SMSTemplate(models.Model):
    TemplateID = models.AutoField(primary_key=True)
    TemplateName = models.CharField(max_length=255)
    TemplateMessage = models.TextField()
    Status = models.CharField(max_length=20, choices=(
        ('active', 'Active'),
        ('not_active', 'Not Active'),
    ))
    CreatedDateTime = models.DateTimeField(auto_now_add=True)
    LastUpdatedDateTime = models.DateTimeField(auto_now=True)
    CCTO = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.TemplateName
