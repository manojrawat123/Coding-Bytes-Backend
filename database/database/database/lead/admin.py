from django.contrib import admin
from .models import Lead

class LeadAdmin(admin.ModelAdmin):
    list_display = ('LeadName', 'LeadPhone', 'LeadEmail', 'LeadLocation', 'LeadAddress',
                    'LeadSource',  'Brand', 'Company', 'Profession',
                    'PageSource', 'Plateform', 'LeadDateTime', 'LeadStatus', 'DND',
                    'LeadRepresentativePrimary', 'LeadRepresentativeSecondary',
                    'LeadCountry', 'LeadState', 'LeadAssignmentAlgo', 'LeadNextCallDate')
    
    list_filter = ('LeadSource', 'Brand', 'Company', 'LeadDateTime', 'LeadStatus', 'DND')
    search_fields = ('LeadName', 'LeadPhone', 'LeadEmail', 'LeadLocation', 'LeadAddress',
                     'Brand__name', 'Company__name', 'LeadRepresentativePrimary',
                     'LeadRepresentativeSecondary')

    # Add any related fields you want to search on
    filter_horizontal = ('LeadServiceInterested',)

admin.site.register(Lead, LeadAdmin)
