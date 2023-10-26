from rest_framework import serializers
# from emailshedule.models import EmailSchedule
from messagelog.models import MessageLog

class MessageLogSerializer(serializers.Serializer):
    template_id = serializers.CharField(max_length=200)
    phone = serializers.ListField(child=serializers.IntegerField(), required=True)
    body = serializers.CharField(max_length=5000)


class MessageLogSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageLog
        fields = "__all__"