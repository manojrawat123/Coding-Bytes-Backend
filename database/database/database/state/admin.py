from django.contrib import admin
from .models import State

class StateAdmin(admin.ModelAdmin):
    list_display = ('ID', 'Country', 'StateName', 'StateCode', 'Active')
    list_filter = ('Country', 'Active')
    search_fields = ('Country', 'StateName', 'StateCode')
    list_per_page = 20

admin.site.register(State, StateAdmin)
