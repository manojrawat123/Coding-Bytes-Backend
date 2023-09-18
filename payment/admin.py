from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'name', 'email', 'payment_amount', 'payment_status', 'payment_date')
    list_filter = ('payment_status', 'payment_currency', 'payment_date')
    search_fields = ('name', 'email', 'payment_confirmation_id')
    readonly_fields = ('payment_id', 'payment_confirmation_id')
    list_per_page = 20

admin.site.register(Payment, PaymentAdmin)