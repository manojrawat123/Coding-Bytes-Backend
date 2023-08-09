from rest_framework import serializers
from service.models import Service

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
