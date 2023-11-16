from django.db import models
from company.models import Company
from brand.models import Brand
from multiselectfield import MultiSelectField

# Create your models here.
class PaymentType(models.Model):
    payment_type_id = models.AutoField(primary_key=True)
    payment_type_display = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    PAYMENT_TYPE_CHOICES = [
        ('Registration', 'Registration'),
        ('Latefee', 'Latefee'),
        ('1st installment', '1st installment'),
        ('2nd installment', '2nd installment'),
    ]

    payment_type = MultiSelectField(choices=PAYMENT_TYPE_CHOICES,max_choices=4)
    payment_type_status = models.CharField(max_length=10, default='Active')

    def __str__(self):
        return self.payment_type_display