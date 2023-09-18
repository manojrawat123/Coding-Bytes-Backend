from django.db import models
from lead.models import Lead
from company.models import Company
from brand.models import Brand
from paymentmode.models import PaymentMode
from paymenttype.models import PaymentType
from service.models import Service 

# Create your models here.
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_confirmation_id = models.CharField(max_length=50)
    customer_id = models.CharField(max_length=50, blank=True)
    lead_id = models.ForeignKey(Lead, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    payment_date = models.DateTimeField()
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_currency = models.CharField(max_length=10)
    payment_purpose = models.ForeignKey(Service, on_delete=models.CASCADE)
    payment_purpose_name = models.CharField(max_length=200)
    payment_type_id = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=1000)
    payment_mode_id = models.ForeignKey(PaymentMode, on_delete=models.CASCADE)
    payment_mode = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=20, default='Approved')
    payment_current_status = models.CharField(max_length=20, default='Active')