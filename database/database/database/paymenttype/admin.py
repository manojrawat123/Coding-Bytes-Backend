from django.contrib import admin
from .models import PaymentType

class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ('payment_type_id', 'payment_type', 'payment_type_display', 'payment_type_status')
    list_filter = ('payment_type', 'payment_type_status')
    search_fields = ('payment_type_display',)
    list_per_page = 20

admin.site.register(PaymentType, PaymentTypeAdmin)
