from rest_framework import serializers
from convertedstudent.models import convertedstudent
from payment.serializers import PaymentGetSerializers
from lead.serializer import LeadGetSerializer,LeadSerializer
from service.serializers import ServiceSerializer


# Please Don't Toch this code It will Effect the whole Data
class ConvertedStudentGetSerializer(serializers.ModelSerializer):
    CourseID = ServiceSerializer()
    PaymentID = PaymentGetSerializers()
    class Meta:
        model = convertedstudent
        fields = '__all__'


class ConvertedStudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = convertedstudent
        fields = '__all__'