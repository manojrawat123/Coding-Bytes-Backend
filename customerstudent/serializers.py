from rest_framework import serializers
from customerstudent.models import Customer
from lead.serializer import LeadGetSerializer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class CustomerGetSerializer(serializers.ModelSerializer):
    # CustomerPhoto = serializers.SerializerMethodField()
    LeadID = LeadGetSerializer()
    class Meta:
        model = Customer
        fields = '__all__'
    
    