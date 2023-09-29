from django.contrib import admin
from batch.models import Batch  


class BatchAdmin(admin.ModelAdmin):
    list_display = ('BatchID', 'BatchName', 'BatchDescription', 'BatchMode', 'BatchTags', 'BatchTeacher', 'BatchStartDate', 'BatchEndDate', 'BatchTime', 'BatchEndTime', 'Status')
    list_filter = ('BatchMode', 'BatchTags', 'Status')
    search_fields = ('BatchName', 'BatchDescription')
    date_hierarchy = 'BatchCreatedDate'

    # Customize the form for adding and editing Batch objects
    fieldsets = (
        ('Basic Information', {
            'fields': ('BatchName', 'BatchDescription', 'BatchMode', 'BatchTags', 'BatchTeacher', 'Status')
        }),
        ('Schedule Information', {
            'fields': ('BatchStartDate', 'BatchEndDate', 'BatchTime', 'BatchEndTime')
        }),
    )

    # Customize the ordering of Batch objects in the admin panel
    ordering = ['-BatchCreatedDate']

# Register the Batch model with the custom admin class
admin.site.register(Batch, BatchAdmin)
