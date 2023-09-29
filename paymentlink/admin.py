from django.contrib import admin
from paymentlink.models import PaymentLink

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('ID', 'Package', 'Amount', 'RepID', 'RepName', 'Status')
    list_filter = ('Status',)
    search_fields = ('Package', 'RepName')

admin.site.register(PaymentLink, PaymentAdmin)
