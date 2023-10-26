from django.contrib import admin
from .models import EmailTemplate

@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'TemplateID',
        'TemplateName',
        'TemplateMessage',
        'Status',
        'CreatedDateTime',
        'LastUpdatedDateTime',
        'CCTO',
    )
    list_filter = ('Status',)
    search_fields = ('TemplateName', 'TemplateMessage', 'CCTO')
    list_per_page = 20
