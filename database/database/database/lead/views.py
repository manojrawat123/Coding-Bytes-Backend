from django.shortcuts import render
from rest_framework.views import APIView
from myuser.renders import UserRenderer
from lead.serializer import LeadSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated
from lead.models import Lead
from rest_framework.generics import RetrieveAPIView



# Create your views here.
class LeadAddView(APIView):
    renderer_classes = [UserRenderer]
    # permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = LeadSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email_from = settings.EMAIL_HOST_USER
            email = "positive.mind.123456789@gmail.com"
            recipient_list = [email,]
            subject = "Lead Add Sucessfully"
            
            data = serializer.save()
            lead_name = serializer.data.get('LeadName', 'Student')
            message = f''''
            Dear {lead_name},
                  We Have recived Payment of 5000 Rupees on Date 07-08-2023 
                  {serializer}'''
            send_mail(subject, message, email_from, recipient_list)
            return Response({"msg": "Registration Sucessfully"})
        
        return Response({"error": "Invalid Data" }, status=status.HTTP_400_BAD_REQUEST)
    
class LeadDetailView(RetrieveAPIView):
    renderer_classes = [UserRenderer]
    
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()


