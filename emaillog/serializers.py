from rest_framework import serializers
# from emailshedule.models import EmailSchedule
from emaillog.models import EmailLog

# class EmailSheduleSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = EmailSchedule
#         fields = "__all__"


class EmailLogSerializer(serializers.Serializer):
    template_id = serializers.CharField(max_length=200)
    emails = serializers.ListField(child=serializers.EmailField(), required=True)
    subject = serializers.CharField(max_length=1000)
    body = serializers.CharField(max_length=5000)


class EmailLogSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailLog
        fields = "__all__"