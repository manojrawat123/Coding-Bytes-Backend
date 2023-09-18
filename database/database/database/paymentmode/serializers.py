from rest_framework import serializers
from paymentmode.models import PaymentMode

class PaymentModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMode
        fields = '__all__'
