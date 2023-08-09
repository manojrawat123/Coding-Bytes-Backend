from django.contrib import admin
from brand.models import Brand

class BrandAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = [field.name for field in Brand._meta.get_fields()]
=======
    list_display = (
        'BrandShortCode',
        'Company',
        'BrandName',
        'BrandAddress',
        'BrandPhone',
        'BrandEmail',
        'BrandLocation',
        'BrandWebsite',
        'BrandNewLeadAddAPI',
        'BrandSMSID',
        'BrandSMSGateway',
        'BrandSMSAPIKey',
        'BrandEMailGateway',
        'BrandEMailAPIKey',
        'BrandEMailRegisteredID',
        'BrandPaymentGatway',
        'BrandPaymentGatwayAPIKey',
        'BrandPaymentGatwayAuthToken',
        'BrandPaymentGatwayRegisteredID',
        'BrandPaymentGatwayRedirectURL',
        'BrandPaymentGatwayWebhookURL',
        'BrandThankYouURL',
        'BrandFacebookPageID',
        'BrandFacebookPageAccessToken',
        'BrandWebDisplay',
        'BrandRecaptchaSecret',
        'BrandClassMode',
    )

    search_fields = ('BrandShortCode', 'BrandName', 'BrandEmail')
    list_filter = ('Company',)  
>>>>>>> bbddb05 (Upadted Version 1.0)

admin.site.register(Brand, BrandAdmin)
