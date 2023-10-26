from rest_framework import serializers
from emailshedule.models import EmailSchedule

class EmailSheduleSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmailSchedule
        fields = "__all__"


class EmailSerializer(serializers.Serializer):
    template_id = serializers.CharField(max_length=200)
    emails = serializers.ListField(child=serializers.EmailField(), required=True)
    subject = serializers.CharField(max_length=1000)
    body = serializers.CharField(max_length=5000)


    