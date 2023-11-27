from django.db import models
from lead.models import Lead
from convertedstudent.models import convertedstudent
from batch.models import Batch
from customerstudent.models import Customer

class BatchStudent(models.Model):
    ID = models.AutoField(primary_key=True)
    BatchID = models.ForeignKey(Batch, on_delete=models.CASCADE)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ConvertedID = models.ForeignKey(convertedstudent, on_delete=models.CASCADE)
    LeadId = models.ForeignKey(Lead, on_delete=models.CASCADE)

    def __str__(self):
        return f"Conversion ID: {self.ID}"