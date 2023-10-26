from rest_framework import serializers
from messageshedule.models import MessageSchedule 

class MessageSheduleSerializers(serializers.ModelSerializer):
    class Meta:
        model = MessageSchedule
        fields = "__all__"


class MessageSerializer(serializers.Serializer):
    template_id = serializers.CharField(max_length=200)
    numbers = serializers.ListField(child=serializers.IntegerField(), required=True)
    body = serializers.CharField(max_length=5000)


    