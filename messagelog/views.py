from django.shortcuts import render
from messagelog.serializers import MessageLogSaveSerializer,MessageLogSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import datetime
from django.conf import settings
from django.core.mail import send_mail ,EmailMessage 
from django.conf import settings
from twilio.rest import Client 
    
class MessageLogSheduleOnlyEmail(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk=None):
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        serializers = MessageLogSerializer(data=request.data)
        if serializers.is_valid():
            try:
                phone_list = serializers.validated_data.get("phone")
                message_body = serializers.validated_data.get("body")
                from_phone = settings.TWILIO_PHONE_NUMBER 
                for recipient_number in phone_list:
                    # Send an SMS to each recipient
                    message = client.messages.create(
                        body=message_body,
                        from_=from_phone,
                        to= "+"+f"{recipient_number}"
                    )
                return Response({"Msg": "Message Send Successfully!!"})
            except Exception as e:
                print(f"SMS sending failed: {e}")
                return Response({"msg": "SMS Failed"})
        return Response(serializers.errors, status=400)
    

    
class SaveMessageInLog(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk=None):
        serializers = MessageLogSaveSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"Msg": "Message Send And data Updated"})