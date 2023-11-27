from django.db import models
from company.models import Company
from brand.models import Brand
from myuser.models import MyUser
from lead.models import Lead
from service.models import Service
from django.utils import timezone

# Create your models here.
class LeadFollowUp(models.Model):
    LeadFollowupID = models.AutoField(primary_key=True)
    LeadID = models.ForeignKey(Lead, on_delete=models.CASCADE)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    LeadFollowupCreatedDate = models.DateTimeField(auto_now_add=True)
    LeadPhonePicked = models.CharField(
        max_length=2000,
        choices=[
            ("Yes", "Yes"),
            ("No", "No")
        ],
        null=True)
    LeadStatus = models.CharField(
        max_length=2000,
        choices=[
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
        ],
        null=True
    )
    LeadStatusDate = models.DateTimeField(default=timezone.now, blank=True,null=True)
    LeadEvent = models.CharField(
        max_length=20,
        choices=[
            ('Visit happened', 'Visit happened'),
            ('Demo happened', 'Demo happened'),
        ],
        null=True, blank=True
    )
    LeadEventDate = models.DateTimeField(null=True, blank=True)
    LeadRep = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    LeadComments = models.TextField(null=True)
    LeadEventTakenBy = models.CharField(max_length=100)
    LeadFeeOffered = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    LeadReasonPhoneNotPicked = models.TextField(null=True, blank=True)
    LeadServiceInterested = models.ForeignKey(Service,on_delete=models.CASCADE)

    def __str__(self):
        return f"Lead {self.LeadID}"
    

