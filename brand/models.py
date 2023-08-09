from django.db import models
from company.models import Company

# Create your models here.
class Brand(models.Model): 
    BrandShortCode = models.CharField(max_length=10)
<<<<<<< HEAD
    CompanyID = models.ForeignKey(Company, on_delete=models.CASCADE)
=======
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
>>>>>>> bbddb05 (Upadted Version 1.0)
    BrandName = models.CharField(max_length=100)
    BrandAddress = models.TextField()
    BrandPhone = models.CharField(max_length=20)
    BrandEmail = models.EmailField()
    BrandLocation = models.CharField(max_length=100)
    BrandWebsite = models.URLField(blank=True, null=True)
    BrandNewLeadAddAPI = models.URLField(blank=True, null=True)
    BrandSMSID = models.CharField(max_length=100, blank=True, null=True)
    BrandSMSGateway = models.CharField(max_length=100, blank=True, null=True)
    BrandSMSAPIKey = models.CharField(max_length=100, blank=True, null=True)
    BrandEMailGateway = models.CharField(max_length=100, blank=True, null=True)
    BrandEMailAPIKey = models.CharField(max_length=100, blank=True, null=True)
    BrandEMailRegisteredID = models.CharField(max_length=100, blank=True, null=True)
    BrandPaymentGatway = models.CharField(max_length=100, blank=True, null=True)
    BrandPaymentGatwayAPIKey = models.CharField(max_length=100, blank=True, null=True)
    BrandPaymentGatwayAuthToken = models.CharField(max_length=100, blank=True, null=True)
    BrandPaymentGatwayRegisteredID = models.CharField(max_length=100, blank=True, null=True)
    BrandPaymentGatwayRedirectURL = models.URLField(blank=True, null=True)
    BrandPaymentGatwayWebhookURL = models.URLField(blank=True, null=True)
    BrandThankYouURL = models.URLField(blank=True, null=True)
    BrandFacebookPageID = models.CharField(max_length=100, blank=True, null=True)
    BrandFacebookPageAccessToken = models.CharField(max_length=200, blank=True, null=True)
    BrandWebDisplay = models.CharField(max_length=100, blank=True, null=True)
    BrandRecaptchaSecret = models.CharField(max_length=200, blank=True, null=True)
<<<<<<< HEAD
    BrandClassMode = models.CharField(max_length=20, blank=True, null=True)
=======
    BrandClassMode = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return self.BrandName
>>>>>>> bbddb05 (Upadted Version 1.0)
