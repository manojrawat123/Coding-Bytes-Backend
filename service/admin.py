from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id','ServiceName', 'ServiceType', 'ServiceWebDisplay', 'Brand', 'Company', 'ServiceStatus')
    list_filter = ('ServiceType', 'Brand', 'Company', 'ServiceStatus')
    search_fields = ('ServiceName', 'Brand', 'Company')  # Add any fields you want to search on

admin.site.register(Service, ServiceAdmin)

