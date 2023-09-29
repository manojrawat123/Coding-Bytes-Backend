from rest_framework import serializers
from refundfees.models import FeeRefund

class RefundFeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeRefund
        fields = '__all__'