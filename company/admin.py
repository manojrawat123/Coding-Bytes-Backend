from django.contrib import admin
from .models import Company

# Custom admin class to display all fields in the admin interface
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        'CompanyShortCode',
        'CompanyName',
        'CompanyPhone',
        'CompanyEmail',
        'CompanyAddress',
        'CompanyPrimaryContactName',
        'CompanyPrimaryContactPhone',
        'CompanyPrimaryContactEmail',
        'CompanyStatus',
    )

# Register the Company model with the custom admin class
admin.site.register(Company, CompanyAdmin)
