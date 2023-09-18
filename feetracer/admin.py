from django.contrib import admin
from .models import Fee

@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        #   'lead', 
        'fee_received', 'fee_created_datetime', 'fee_payment_datetime',
        # 'receipt_number', 'student', 'payment_mode', 'representative', 'payment_type',
        # 'customer_status', 'company', 'brand', 'converted_id', 'updated_by', 'payment_id'
    )
    # list_filter = ('customer_status', 'company', 'brand', 'payment_type')
    # search_fields = ('lead__LeadName', 'student__CustomerName', 'receipt_number')
    # list_per_page = 20
    # autocomplete_fields = ( 'student', 'representative', 'payment_id', 'converted_id')
