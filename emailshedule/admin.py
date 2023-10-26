from django.contrib import admin
from .models import EmailSchedule

@admin.register(EmailSchedule)
class EmailScheduleAdmin(admin.ModelAdmin):
    list_display = (
        'ScheduleID',
        'ScheduleDateTime',
        'get_customer_names',
        'ScheduleTemplate',
    )
    list_filter = ('ScheduleDateTime', 'ScheduleTemplate')
    list_per_page = 20

    def get_customer_names(self, obj):
        return ", ".join([customer.CustomerName for customer in obj.ScheduleCustomers.all()])

    get_customer_names.short_description = 'Scheduled Customers'
