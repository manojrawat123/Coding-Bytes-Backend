from django.contrib import admin
from .models import convertedstudent

@admin.register(convertedstudent)
class ConvertedStudentAdmin(admin.ModelAdmin):
    list_display = (
        'ConvertedID', 'LeadID', 'CourseName', 'ClassMode', 'CourseStartDate',
        'CourseEndDate', 'TotalFee', 'StudentID', 'UpdateBY', 'Representative',
        'CustomerStatus', 'LostSales'
    )
    list_filter = ('ClassMode', 'CourseStartDate', 'CustomerStatus')
    search_fields = ('LeadID__LeadName', 'StudentID__CustomerName', 'Representative__username')
    list_per_page = 20
    autocomplete_fields = ('LeadID', 'StudentID', 'Representative')
    raw_id_fields = ('Brand', 'Company', 'PaymentID')

    def get_queryset(self, request):
        return super().get_queryset(request).select_related(
            'LeadID', 'StudentID', 'Representative'
        )