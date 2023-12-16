from rest_framework import serializers
# from emailshedule.models import EmailSchedule
from messagelog.models import MessageLog
from messagetemplate.serializers import MessageTemplateSerializers

class MessageLogSerializer(serializers.ModelSerializer):
    TemplateID = MessageTemplateSerializers()
    class Meta:
        model = MessageLog
        fields = "__all__"

class MessageLogSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageLog
        fields = "__all__"