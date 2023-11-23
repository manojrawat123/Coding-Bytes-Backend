from django.db import models
from brand.models import Brand
from company.models import Company
from lead.models import Lead
from paymentmode.models import PaymentMode
from myuser.models import MyUser
from paymenttype.models import PaymentType
from customerstudent.models import Customer
from payment.models import Payment
from convertedstudent.models import convertedstudent

# Create your models here.
class Fee(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    fee_received = models.DecimalField(max_digits=10, decimal_places=2)
    fee_created_datetime = models.DateField()
    fee_payment_datetime = models.DateField()
    receipt_number = models.CharField(max_length=50)
    student = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='fees')
    payment_mode = models.ForeignKey(PaymentMode, on_delete=models.CASCADE)
    representative = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    customer_status = models.CharField(max_length=100, default="Active")
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    converted_id = models.ForeignKey(convertedstudent, on_delete=models.CASCADE, related_name='converted_fees')
    updated_by = models.CharField(max_length=100)
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Fee - {self.id}"