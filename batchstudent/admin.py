from django.contrib import admin
from batchstudent.models import BatchStudent

class BatchStudentAdmin(admin.ModelAdmin):
    list_display = ('ID', )

admin.site.register(BatchStudent, BatchStudentAdmin)
