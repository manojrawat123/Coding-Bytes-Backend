from django.db import models

# Create your models here.

class Company(models.Model):
    CompanyShortCode = models.CharField(max_length=10)
    CompanyName = models.CharField(max_length=100)
    CompanyPhone = models.BigIntegerField()
    CompanyEmail = models.EmailField()
    CompanyAddress = models.TextField()
    CompanyPrimaryContactName = models.CharField(max_length=100)
    CompanyPrimaryContactPhone = models.BigIntegerField()
    CompanyPrimaryContactEmail = models.EmailField()
<<<<<<< HEAD
    CompanyStatus = models.CharField(max_length=20)
=======
    CompanyStatus = models.CharField(max_length=20)

    def __str__(self):
        return self.CompanyName
>>>>>>> bbddb05 (Upadted Version 1.0)
