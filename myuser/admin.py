from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from myuser.models import MyUser

# Register your models here.
class UserAdmin(BaseUserAdmin):
    list_display = ["email", "name", "phone", "is_admin",  "company", "is_active"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["email", "password", "company", "brand","is_active"]}),
        ("Personal info", {"fields": ["name", "phone"]}),
        ("Permissions", {"fields": ["is_admin"]}),
        ("Additional Info", {"fields": ["status", "online_status", "designation", "user_location", "last_login", ]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name", "phone", "password1", "password2" ,"company", "brand","dob", "doj","user_type"],
            },
        ),
    ]
    search_fields = ["email", "name", "phone"]
    ordering = ["email"]
    filter_horizontal = []


admin.site.register(MyUser, UserAdmin)