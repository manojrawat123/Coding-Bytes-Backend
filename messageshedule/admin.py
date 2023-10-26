from django.contrib import admin
from messageshedule.models import MessageSchedule

@admin.register(MessageSchedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('ScheduleID', 'ScheduleDateTime', 'Status')

