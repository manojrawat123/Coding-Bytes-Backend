from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('CustomerID', 'CustomerName', 'Company', 'Brand', 'LeadID', 'Attendance','CustomerPhoto')
    list_filter = ('Company', 'Brand', 'LeadID', 'Attendance')
    search_fields = ('CustomerName', 'CustomerPhone', 'CustomerEmail')
    list_per_page = 20
