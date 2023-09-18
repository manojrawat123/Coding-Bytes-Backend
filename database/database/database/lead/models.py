from django.db import models
from brand.models import Brand
from company.models import Company
from service.models import Service

# Create your models here.
class Lead(models.Model):
    LeadName = models.CharField(max_length=100)
    LeadPhone = models.CharField(max_length=20)
    LeadEmail = models.EmailField()
    LeadLocation = models.CharField(max_length=100)
    LeadAddress = models.CharField(max_length=200)
    LeadSource = models.CharField(max_length=100)
    LeadServiceInterested = models.ManyToManyField(Service)
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    Profession = models.CharField(max_length=200)
    PageSource = models.CharField(max_length=100)
    Plateform = models.CharField(max_length=100)
    LeadDateTime = models.DateTimeField()
    LeadStatus = models.CharField(max_length=50)
    DND = models.BooleanField(default=False)
    LeadRepresentativePrimary = models.CharField(max_length=100)
    LeadRepresentativeSecondary = models.CharField(max_length=100)
    LeadCountry = models.CharField(max_length=100)
    LeadState = models.CharField(max_length=100)
    LeadAssignmentAlgo = models.CharField(max_length=100)
    LeadNextCallDate = models.DateField()
    # Add other fields for Lead model as needed