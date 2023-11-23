from django.db import models
from lead.models import Lead
from customerstudent.models import Customer
from myuser.models import MyUser
from brand.models import Brand
from company.models import Company
from payment.models import Payment
from service.models import Service

class convertedstudent(models.Model): 
    ConvertedID = models.AutoField(primary_key=True)
    LeadID = models.ForeignKey(Lead, on_delete=models.CASCADE)
    CourseName = models.CharField(max_length=255)
    ClassMode = models.CharField(max_length=2000,
        choices=[
            ("Online", "Online"),
            ("Offline", "Offline")
        ],
    )
    CourseID = models.ForeignKey(Service, on_delete=models.CASCADE)
    CreatedDateTime = models.DateTimeField(auto_now_add=True)
    ConvertedDateTime = models.DateTimeField(auto_now_add=True)
    CourseStartDate = models.DateField() 
    CourseEndDate = models.DateField()
    CourseExpiryDate = models.DateField(null=True, blank=True)
    TotalFee = models.DecimalField(max_digits=10, decimal_places=2)
    StudentID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    NextDueDate = models.DateField()
    UpdateBY = models.CharField(max_length=100)
    Representative = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    PaymentID = models.ForeignKey(Payment, on_delete=models.CASCADE)
    CustomerStatus = models.CharField(max_length=20, default="Active")
    LostSales = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    LostSalesDate = models.DateField(null=True, blank=True)
    LostSalesReason = models.TextField(null=True,blank=True)
    SecureKey = models.CharField(max_length=100, null=True, blank=True)