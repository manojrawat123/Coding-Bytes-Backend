from django.db import models
from brand.models import Brand
from company.models import Company
from service.models import Service
from leadScource.models import LeadSource
from myuser.models import MyUser

# Create your models here.
class Lead(models.Model):
    LeadName = models.CharField(max_length=100)
    LeadPhone = models.CharField(max_length=20)
    LeadEmail = models.EmailField()
    LeadLocation = models.CharField(max_length=100)
    LeadAddress = models.CharField(max_length=200)
    LeadScourceId = models.ForeignKey(LeadSource, on_delete=models.CASCADE)
    LeadSource = models.CharField(max_length=100)
    LeadServiceInterested = models.ManyToManyField(Service)
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    Profession = models.CharField(max_length=200)
    PageSource = models.CharField(max_length=100)
    Plateform = models.CharField(max_length=100)
    LeadDateTime = models.DateTimeField()
    LeadStatus = models.CharField(max_length=50, choices=[
            ('Fresh', 'Fresh'),
            ('Ready To Enroll', 'Ready To Enroll'),
            ('Visit scheduled', 'Visit scheduled'),
            ('Demo scheduled', 'Demo scheduled'),
            ("Highly Intersted", "Highly Intersted"),
            ("Least Intersted", "Least Intersted"),
            ("Distance Issue", "Distance Issue"),  
            ("Pricing Issue", "Pricing Issue"),    
            ("Already Taken Service", "Already Taken Service"),  
            ("Quality Issue", "Quality Issue"),    
            ("Not Interested Anymore", "Not Interested Anymore"),  
            ("Did Not Enquire", "Did Not Enquire"),  
            ("Only Wanted Information", "Only Wanted Information"),  
            ("Other", "Other"), 
            ("Try Next Time", "Try Next Time"), 
            
        ])
    DND = models.BooleanField(default=False)
    LeadRepresentativePrimary = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='LeadRepresentativePrimary')
    LeadRepresentativeSecondary = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='LeadRepresentativeSecondary')
    LeadCountry = models.CharField(max_length=100)
    LeadState = models.CharField(max_length=100)
    LeadAssignmentAlgo = models.CharField(max_length=100)
    LeadNextCallDate = models.DateField()