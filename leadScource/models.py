from django.db import models
from company.models import Company
from brand.models import Brand

# Create your models here.
class LeadSource(models.Model):
    LeadSourceID = models.AutoField(primary_key=True)
    LeadSource = models.CharField(max_length=50, choices=[
        ('Incoming', 'Incoming'),
        ('Facebook', 'Facebook'),
        ('Google', 'Google'),
        # Add other lead source choices as needed
    ])
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    Status = models.CharField(max_length=20, default='Active')
    DisplayStatus = models.BooleanField(default=True)

    def __str__(self):
        return self.LeadSource