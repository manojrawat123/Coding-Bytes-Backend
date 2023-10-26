from django.contrib import admin
from messagelog.models import MessageLog 

@admin.register(MessageLog)
class MessageLogAdmin(admin.ModelAdmin):
    list_display = ('LogID', 'Date', 'TemplateID', 'Attachment')
    list_filter = ('Date', 'TemplateID', 'CompanyID')
    search_fields = ('LogID', 'Date', 'TemplateID__TemplateName', 'CompanyID__company_name')
