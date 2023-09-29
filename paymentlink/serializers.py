from rest_framework import serializers
from paymentlink.models import PaymentLink

class PaymentLinkSerializers(serializers.ModelSerializer):
    class Meta:
        model = PaymentLink
        fields = '__all__'