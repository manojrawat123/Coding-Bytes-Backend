from django.db import models
from lead.models import Lead
from paymentmode.models import PaymentMode
from convertedstudent.models import convertedstudent
from customerstudent.models import Customer
from payment.models import Payment
from paymenttype.models import PaymentType
from company.models import Company
from brand.models import Brand
from myuser.models import MyUser
from django.utils import timezone


class FeeRefund(models.Model):
    FeeRefundID = models.AutoField(primary_key=True)
    LeadID = models.ForeignKey(Lead, on_delete=models.CASCADE)
    FeeRefunded = models.DecimalField(max_digits=10, decimal_places=2)
    FeeRefundedCreatedDateTime = models.DateTimeField(default = timezone.now)
    FeeRefundedDateTime = models.DateTimeField(default=timezone.now)
    ReceiptNumber = models.CharField(max_length=20, null=True)
    PaymentMode = models.ForeignKey(PaymentMode, on_delete=models.CASCADE)
    StudentID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ConvertedID = models.ForeignKey(convertedstudent, on_delete=models.CASCADE)
    UpdatedBY = models.CharField(max_length=400)
    Representative = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    PaymentID = models.ForeignKey(Payment, on_delete=models.CASCADE)
    PaymentType = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    CustomerStatus = models.CharField(max_length=20, default="Active")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)