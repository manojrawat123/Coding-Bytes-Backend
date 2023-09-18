from django.db import models
from company.models import Company
from brand.models import Brand


class PaymentMode(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    payment_mode_id = models.AutoField(primary_key=True)
    
    PAYMENT_MODE_CHOICES = [
        ('PayTM', 'PayTM'),
        ('Swipe Machine', 'Swipe Machine'),
        ('Cash', 'Cash'),
        ('Bank Transfer', 'Bank Transfer'),
    ]
    
    payment_mode = models.CharField(choices=PAYMENT_MODE_CHOICES, max_length=1000)
    payment_mode_display = models.CharField(max_length=100)
    payment_mode_status = models.BooleanField() 
    class Meta:
        unique_together = ('brand', 'payment_mode')