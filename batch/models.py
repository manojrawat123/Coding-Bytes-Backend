from django.db import models
from myuser.models import MyUser

class Batch(models.Model):
    BatchID = models.AutoField(primary_key=True)
    BatchName = models.CharField(max_length=255)
    BatchDescription = models.TextField()
    BatchMode = models.CharField(max_length=10, choices=[('Offline', 'Offline'), ('Online', 'Online')])
    BATCH_TAGS_CHOICES = [
        ('MWF', 'MWF'),
        ('TTS', 'TTS'),
        ('Weekdays', 'Weekdays'),
        ('Weekends', 'Weekends'),
    ]
    BatchTags = models.CharField(max_length=20, choices=BATCH_TAGS_CHOICES)
    BatchTeacher = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    BatchTeacherName = models.CharField(max_length=200)
    BatchStaffAssigned = models.CharField(max_length=300)
    BatchCreatedDate = models.DateTimeField(auto_now_add=True)
    BatchStartDate = models.DateTimeField()
    BatchEndDate = models.DateTimeField()
    BatchTime = models.TimeField()
    BatchEndTime = models.TimeField()
    Status = models.BooleanField(default=True)