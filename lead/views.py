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
from datetime import datetime, timedelta
from django.utils import timezone

# Create your views here.
class LeadAddView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = LeadSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                # Save data to the database
                data = serializer.save()
                # Email sending logic
                email_from = settings.EMAIL_HOST_USER
                email = "positive.mind.123456789@gmail.com"
                recipient_list = [email,]
                subject = "Lead Add Successfully" 

                lead_name = serializer.data.get('LeadName', 'Student')
                message = f'''
                Dear {lead_name},
                We Have received Payment of 5000 Rupees on Date 07-08-2023 
                {serializer}'''
                send_mail(subject, message, email_from, recipient_list)
                # Return a success response
                return Response(serializer.data)
            
            except Exception as e:
                # Handle exceptions related to email sending here
                # You can log the error for debugging purposes
                print(f"Email sending failed: {e}")
                
            # If the code reaches this point, it means that the data is saved in the database
            return Response(serializer.data)
        else:
            # Handle validation errors if the serializer is not valid
            return Response({"error": "Validation failed", "details": serializer.errors})
    def get(self, request, id = None):
        if id is not None:
            lead = Lead.objects.get(id=id) 
            serializer = LeadSerializer(lead)
            return Response(serializer.data)
        lead = Lead.objects.all() 
        serializer = LeadSerializer(lead, many=True)
        return Response(serializer.data)
    def put(self, request, id=None):
        if id is None:
            return Response({"Msg": "Id is None"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            lead_instance = Lead.objects.get(id=id)
        except Lead.DoesNotExist:
            return Response({"Msg": "Lead not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = LeadSerializer(lead_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Msg":" Updated Sucessfully!!"})
    
class LeadDetailView(RetrieveAPIView):
    renderer_classes = [UserRenderer]     
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()


