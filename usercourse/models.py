from django.db import models
from myuser.models import MyUser
from service.models import Service
from company.models import Company
from brand.models import Brand

class UserCourse(models.Model):
    UserID = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    CourseID = models.ForeignKey(Service, on_delete=models.CASCADE)
    CompanyID = models.ForeignKey(Company, on_delete=models.CASCADE)
    BrandID = models.ForeignKey(Brand, on_delete=models.CASCADE)
    Status = models.CharField(
        max_length=20,
        choices=[
            ('Active', 'Active'),
            ('InActive', 'InActive'),
        ]
    )
    DefaultPriority = models.PositiveIntegerField(default=10)
    CourseWeightage = models.PositiveIntegerField(default=10)
