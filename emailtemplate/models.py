from django.db import models

class EmailTemplate(models.Model):
    TemplateID = models.AutoField(primary_key=True)
    TemplateName = models.CharField(max_length=100)
    TemplateMessage = models.CharField(max_length=255)
    TemplateBody = models.TextField()
    Status = models.CharField(max_length=10, default='Active')
    CreatedDateTime = models.DateTimeField(auto_now_add=True)
    LastUpdatedDateTime = models.DateTimeField(auto_now=True)
    CCTO = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.TemplateName 
    

