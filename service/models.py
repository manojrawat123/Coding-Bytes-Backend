from django.db import models
from brand.models import Brand
from company.models import Company

class Service(models.Model):
    ServiceName = models.CharField(max_length=100)
    ServiceType = models.CharField(max_length=50)
    ServiceWebDisplay = models.URLField(max_length=200, blank=True, null=True)
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    ServiceStatus = models.CharField(max_length=20)
    SERVICE_MODE_CHOICES = [
        ('Online', 'Online'),
        ('Offline', 'Offline'),
    ]
    serviceMode = models.CharField(max_length=10, choices=SERVICE_MODE_CHOICES)
    def __str__(self):
        return self.ServiceName
        