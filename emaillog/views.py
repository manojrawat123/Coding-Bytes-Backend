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
        serializers = EmailLogSaveSerializer(data=request.data)
        if serializers.is_valid():
            try: 
                print(request.data["emails"])
                email_lis = request.data["emails"]
                my_subject = request.data["subject"]
                my_body = request.data["body"]
                email_from = settings.EMAIL_HOST_USER
                email = "positive.mind.123456789@gmail.com"
                recipient_list = email_lis
                subject = my_subject
                message = f'''{my_body}'''
                email = EmailMessage(subject, message, email_from,recipient_list)
                email.send() 
                serializers.save()
                return Response({"Msg": "Email Send Successfully!!"})
            except Exception as e:
                print(f"Email sending failed: {e}")
                return Response({"msg": "Email Failed"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializers.errors, status=400)
    
class SaveEmailInLog(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk=None):
        serializers = EmailLogSaveSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"Msg": "Mail Send And data Updated"})