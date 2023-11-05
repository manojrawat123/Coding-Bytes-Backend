from django.db import models


class MenuItem(models.Model):
    ID = models.AutoField(primary_key=True)
    MenuItemDescription = models.CharField(max_length=255)
    MenuType = models.CharField(max_length=10, choices=[('div', 'div'), ('ul', 'ul'), ('li', 'li')])
    MenuLink = models.URLField(default="http://localhost:5173")
    EndPoint = models.CharField(max_length=20)
    PageTitle = models.CharField(max_length=255)
    BrandIDArray = models.CharField(max_length=255)
    Level = models.PositiveIntegerField()
    ParentID = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    MenuIdentifier = models.CharField(max_length=255, null=True, blank=True)
    UserRoles = models.CharField(max_length=255, null=True, blank=True)
    DisplayOrder = models.PositiveIntegerField(null=True, blank=True)
    ActiveStatus = models.CharField(max_length=10, choices=[('Active', 'Active'), ('NonActive', 'NonActive')])
    ArchiveStatus = models.CharField(max_length=10, choices=[('Deleted', 'Deleted')])
    AccessLevel = models.PositiveIntegerField(choices=[(10, '10'), (20, '20'), (30, '30'), (100, '100')])
    CreateUpto = models.PositiveIntegerField(choices=[(10, '10'), (20, '20'), (30, '30'), (100, '100')])
    UpdateUpto = models.PositiveIntegerField(choices=[(10, '10'), (20, '20'), (30, '30'), (100, '100')])
    DeleteUpto = models.PositiveIntegerField(choices=[(10, '10'), (20, '20'), (30, '30'), (100, '100')])

    def __str__(self):
        return self.MenuItemDescription
