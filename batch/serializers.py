from rest_framework import serializers
from batch.models import Batch

class BatchSerializers(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = "__all__"