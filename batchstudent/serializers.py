from rest_framework import serializers
from batchstudent.models import BatchStudent
from batch.serializers import BatchSerializers


class BatchStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BatchStudent
        fields = '__all__'

class BatchStuByConvertedLead(serializers.ModelSerializer):
    BatchID = BatchSerializers()
    class Meta:
        model = BatchStudent
        fields = '__all__'
