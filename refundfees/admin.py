from django.contrib import admin
from refundfees.models import FeeRefund

class FeeRefundAdmin(admin.ModelAdmin):
    list_display = (
        'FeeRefunded',
        'FeeRefundedCreatedDateTime',
        'FeeRefundedDateTime',
        'ReceiptNumber',
        'UpdatedBY',
        'Representative',
        'CustomerStatus',
    )

admin.site.register(FeeRefund, FeeRefundAdmin)
