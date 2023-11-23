from rest_framework import serializers
from payment.models import Payment
from service.serializers import ServiceSerializer
from lead.serializer import LeadGetSerializer
from paymenttype.serializers import PaymentTypeSerializer
from paymentmode.serializers import PaymentModeSerializer

class PaymentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Payment
        fields = '__all__'


class PaymentGetSerializers(serializers.ModelSerializer):
    payment_type_id = PaymentTypeSerializer()
    payment_mode_id = PaymentModeSerializer()
    payment_purpose = ServiceSerializer()
    lead_id = LeadGetSerializer()
    class Meta:
        model = Payment
        fields = '__all__'