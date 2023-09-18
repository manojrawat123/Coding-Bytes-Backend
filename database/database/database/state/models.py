from django.db import models

class State(models.Model):
    ID = models.AutoField(primary_key=True)
    Country = models.CharField(max_length=100)
    StateName = models.CharField(max_length=100)
    StateCode = models.CharField(max_length=10)
    Active = models.BooleanField(default=True)

    def __str__(self):
        return self.StateName
