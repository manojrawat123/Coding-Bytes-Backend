from django.contrib import admin
from .models import PaymentMode

class PaymentModeAdmin(admin.ModelAdmin):
    list_display = ('payment_mode_id', 'payment_mode', 'payment_mode_display', 'payment_mode_status')
    list_filter = ('payment_mode', 'payment_mode_status')
    search_fields = ('payment_mode_display',)
    list_per_page = 20

admin.site.register(PaymentMode, PaymentModeAdmin)
