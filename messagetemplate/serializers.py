from rest_framework import serializers
from messagetemplate.models import SMSTemplate

class MessageTemplateSerializers(serializers.ModelSerializer):
    class Meta:
        model = SMSTemplate
        fields = "__all__"