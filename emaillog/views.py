from django.shortcuts import render
from emaillog.models import EmailLog
from emaillog.serializers import EmailLogSerializer, EmailLogSaveSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import datetime
from django.conf import settings
from django.core.mail import send_mail ,EmailMessage  
    
class EmailLogSheduleOnlyEmail(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk=None):
        serializers = EmailLogSerializer(data=request.data)
        if serializers.is_valid():
            try:
                email_lis = serializers.data.get("emails")
                my_subject = serializers.data.get("subject")
                my_body = serializers.data.get("body")
                email_from = settings.EMAIL_HOST_USER
                email = "positive.mind.123456789@gmail.com"
                recipient_list = email_lis
                subject = my_subject
                message = f'''{my_body}'''
                email = EmailMessage(subject, message, email_from,recipient_list)
                email.send() 
                return Response({"Msg": "Email Send Successfully!!"})
            except Exception as e:
                print(f"Email sending failed: {e}")
                return Response({"msg": "Email Failed"})
        return Response(serializers.errors, status=400)
    
class SaveEmailInLog(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk=None):
        serializers = EmailLogSaveSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"Msg": "Mail Send And data Updated"})