from rest_framework import serializers
from leadScource.models import LeadSource

class LeadScourceSerializers(serializers.ModelSerializer):
    class Meta:
        model = LeadSource
        fields = '__all__'