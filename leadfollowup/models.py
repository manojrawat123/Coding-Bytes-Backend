from django.db import models
from company.models import Company
from brand.models import Brand
from myuser.models import MyUser
from lead.models import Lead

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
            ('Ready To Enroll', 'Ready To Enroll'),
            ('Visit scheduled', 'Visit scheduled'),
            ('Demo scheduled', 'Demo scheduled'),
            ("Highly Intersted", "Highly Intersted"),
            ("Least Intersted", "Least Intersted"),
            ("Distance Issue", "Distance Issue"),  # New choice
            ("Pricing Issue", "Pricing Issue"),    # New choice
            ("Already Taken Service", "Already Taken Service"),  # New choice
            ("Quality Issue", "Quality Issue"),    # New choice
            ("Not Interested Anymore", "Not Interested Anymore"),  # New choice
            ("Did Not Enquire", "Did Not Enquire"),  # New choice
            ("Only Wanted Information", "Only Wanted Information"),  # New choice
            ("Other", "Other"), # Other
        ],
        null=True
    )
    LeadStatusDate = models.DateTimeField(null=True, blank=True)
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
    leadRepName = models.CharField(max_length=200)
    # LeadFollowupRep = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    LeadEventTakenBy = models.CharField(max_length=100)
    LeadFeeOffered = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    LeadReasonPhoneNotPicked = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Lead {self.LeadID}"
    

