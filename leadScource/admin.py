from django.contrib import admin
from .models import LeadSource

class LeadSourceAdmin(admin.ModelAdmin):
    list_display = ('LeadSourceID', 'LeadSource', 'Brand', 'Company', 'Status', 'DisplayStatus')
    list_filter = ('Brand', 'Company', 'Status', 'DisplayStatus')
    search_fields = ('LeadSource', 'Brand__name', 'Company__name')  # Add any related fields you want to search on

admin.site.register(LeadSource, LeadSourceAdmin)
