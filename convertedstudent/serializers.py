from rest_framework import serializers
from convertedstudent.models import convertedstudent

class ConvertedStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = convertedstudent
        fields = '__all__'