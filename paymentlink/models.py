import random
from django.db import models
from myuser.models import MyUser

def generate_unique_url():
    while True:
        random_number = random.randint(1000, 9999)
        url = f"http://localhost:5173/paymentredirectlink/{random_number}"
        if not PaymentLink.objects.filter(PaymentLink=url).exists():
            return url

class PaymentLink(models.Model):
    ID = models.AutoField(primary_key=True)
    Package = models.CharField(max_length=255)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    RepID = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    RepName = models.CharField(max_length=255)
    PaymentLink = models.URLField(unique=True, default=generate_unique_url)
    PaymentAmount = models.DecimalField(max_digits=10, decimal_places=2)
    PaymentLinkCreatedDateTime = models.DateTimeField(auto_now_add=True)
    PaymentLinkExpiryDateTime = models.DateTimeField(null=True, blank=True)
    Status = models.CharField(max_length=50, default="Active")

    def save(self, *args, **kwargs):
        if not self.PaymentLink:
            self.PaymentLink = generate_unique_url()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Payment ID: {self.ID}, Package: {self.Package}, Amount: {self.Amount}, Status: {self.Status}"