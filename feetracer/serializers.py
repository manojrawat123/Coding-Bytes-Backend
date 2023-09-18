from rest_framework import serializers
from feetracer.models import Fee
from paymenttype.models import PaymentType
from paymentmode.serializers import PaymentModeSerializer
from paymenttype.serializers import PaymentTypeSerializer


class FeesSerializerGet(serializers.ModelSerializer):
    payment_mode = PaymentModeSerializer()
    payment_type = PaymentTypeSerializer()
    class Meta:
        model = Fee
        fields = '__all__'


class FeesSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Fee
        fields = '__all__'
