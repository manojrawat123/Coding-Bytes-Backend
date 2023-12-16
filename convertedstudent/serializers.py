from rest_framework import serializers
from convertedstudent.models import convertedstudent
from payment.serializers import PaymentGetSerializers
from lead.serializer import LeadGetSerializer,LeadSerializer
from service.serializers import ServiceSerializer
from brand.serializers import BrandSerializers
from customerstudent.serializers import CustomerSerializer, CustomerGetSerializer


# Please Don't Toch this code It will Effect the whole Data
class ConvertedStudentGetSerializer(serializers.ModelSerializer):
    CourseID = ServiceSerializer()
    PaymentID = PaymentGetSerializers()
    class Meta:
        model = convertedstudent
        fields = '__all__'

class ConvertedStudentGetRealSerializer(serializers.ModelSerializer):
    CourseID = ServiceSerializer()
    PaymentID = PaymentGetSerializers()
    LeadID = LeadGetSerializer()
    Brand = BrandSerializers()
    StudentID = CustomerGetSerializer()
    class Meta:
        model = convertedstudent
        fields = '__all__'
    
class ConvertedStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = convertedstudent
        fields = '__all__'