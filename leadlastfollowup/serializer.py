from rest_framework import serializers
from .models import LeadLastFollowUp

class LeadLastFollowUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadLastFollowUp
        fields = '__all__'