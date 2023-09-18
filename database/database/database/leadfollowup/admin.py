from django.contrib import admin
from .models import LeadFollowUp

class LeadFollowUpAdmin(admin.ModelAdmin):
    list_display = ('LeadFollowupID', 'LeadID', 'Company', 'Brand', 'LeadFollowupCreatedDate', 'LeadStatus', 'LeadEvent')
    list_filter = ('Company', 'Brand', 'LeadStatus', 'LeadEvent')
    search_fields = ('LeadID__name', 'LeadID__email')  # Adjust based on the fields in your Lead model

admin.site.register(LeadFollowUp, LeadFollowUpAdmin)
