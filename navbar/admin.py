from django.contrib import admin
from .models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('MenuItemDescription', 'MenuType', 'MenuLink', 'Level', 'ParentID', 'DisplayOrder', 'ActiveStatus')
    list_filter = ('MenuType', 'Level', 'ActiveStatus')
    search_fields = ('MenuItemDescription', 'PageTitle', 'MenuIdentifier', 'UserRoles')
    ordering = ('Level', 'DisplayOrder')
    list_per_page = 20
    # You can customize this admin class further as needed
