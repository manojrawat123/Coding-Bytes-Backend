from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from myuser.models import MyUser

# Register your models here.
class UserAdmin(BaseUserAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["email", "name", "phone", "is_admin",  "company"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["email", "password", "company", "brand"]}),
        ("Personal info", {"fields": ["name", "phone"]}),
        ("Permissions", {"fields": ["is_admin"]}),
        ("Additional Info", {"fields": ["status", "online_status", "designation", "user_location", "last_login", ]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name", "phone", "password1", "password2" ,"company", "brand"],
            },
        ),
    ]
    search_fields = ["email", "name", "phone"]
    ordering = ["email"]
    filter_horizontal = []


# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)