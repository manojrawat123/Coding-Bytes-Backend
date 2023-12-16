from django.contrib import admin
from .models import SMSTemplate

@admin.register(SMSTemplate)
class SMSTemplateAdmin(admin.ModelAdmin):
    list_display = ('TemplateID', 'TemplateName', 'Status', 'CreatedDateTime', 'LastUpdatedDateTime')
    search_fields = ('TemplateName',)
    list_filter = ('Status',)
    readonly_fields = ('CreatedDateTime', 'LastUpdatedDateTime')
    ordering = ('-CreatedDateTime',)

# 