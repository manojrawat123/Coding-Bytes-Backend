from django.contrib import admin
from .models import SMSTemplate  # Import your model here

@admin.register(SMSTemplate)
class SMSTemplateAdmin(admin.ModelAdmin):
    list_display = ('TemplateID', 'TemplateName', 'Status', 'CreatedDateTime', 'LastUpdatedDateTime')
