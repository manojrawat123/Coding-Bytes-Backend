from django.contrib import admin
from batchstudent.models import BatchStudent

@admin.register(BatchStudent)
class ConversionAdmin(admin.ModelAdmin):
    list_display = ( 'BatchID', 'CustomerID', 'ConvertedID', 'LeadId')
