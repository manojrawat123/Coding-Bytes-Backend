from django.db import models
from company.models import Company
from brand.models import Brand
from lead.models import Lead

class Customer(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    LeadID = models.ForeignKey(Lead, on_delete=models.CASCADE)
    CustomerQRCode = models.CharField(max_length=100, null=True, blank=True)
    Attendance = models.BooleanField(default=False)
    CustomerName = models.CharField(max_length=200)
    CustomerShippingAddress = models.TextField(null=True, blank=True)
    CustomerBillingAddress = models.TextField(null=True, blank=True)
    CustomerGST = models.CharField(max_length=20, null=True, blank=True)
    CustomerLocation = models.CharField(max_length=100, null=True, blank=True)
    CustomerPAN = models.CharField(max_length=20, null=True, blank=True)
    CustomerPhone = models.CharField(max_length=20)
    CustomerEmail = models.EmailField()
    CustomerGender = models.CharField(max_length=200, null=True)
    CustomerDOB = models.DateField(null=True)
    CustomerOccupation = models.CharField(max_length=200, null=True)
    CustomerPhoto = models.ImageField(upload_to="ProfilePhoto", null=True)

    def __str__(self):
        return self.CustomerName