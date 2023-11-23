from rest_framework import serializers
from feetracer.models import Fee
from paymenttype.models import PaymentType
from paymentmode.serializers import PaymentModeSerializer
from paymenttype.serializers import PaymentTypeSerializer
from convertedstudent.serializers import ConvertedStudentGetSerializer
from lead.serializer import LeadGetSerializer

class FeesSerializerGet(serializers.ModelSerializer):
    payment_mode = PaymentModeSerializer()
    payment_type = PaymentTypeSerializer()
    converted_id = ConvertedStudentGetSerializer()
    lead = LeadGetSerializer()
    class Meta:
        model = Fee
        fields = '__all__'


class FeesSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Fee
        fields = '__all__'
