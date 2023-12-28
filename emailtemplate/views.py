from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from emailtemplate.models import EmailTemplate
from emailtemplate.serializers import EmailTemplateSerializers
from rest_framework.permissions import IsAuthenticated
from service.serializers import ServiceSerializer
from service.models import Service
from leadScource.models import LeadSource
from leadScource.serializers import LeadScourceSerializers
from lead.models import Lead
from lead.serializer import LeadGetSerializer

class EmailTemplateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):
        if pk is not None:
            data = EmailTemplate.objects.get(ScheduleID= pk)
            serializer = EmailTemplateSerializers(data)
            return Response(serializer.data)
        else:
            data = EmailTemplate.objects.all()
            serializer = EmailTemplateSerializers(data, many=True)
            return Response(serializer.data)
    
    def post(self, request, pk=None):
        if pk is not None:
            return Response({"Err": "Post Method Not allowed"})
        serializer = EmailTemplateSerializers(data=request.data)
        if serializer.is_valid():
            # Save data to the database
            data = serializer.save()
            # Return a success response
            return Response({"Msg ":"Registration successfully!!"})
        return Response(serializer.errors, status=400)
    
    def put(self, request, pk):
        try:
            email_schedule = EmailTemplate.objects.get(pk=pk)
        except EmailTemplate.DoesNotExist:
            return Response({"error": "EmailSchedule not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmailTemplateSerializers(email_schedule, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Msg": "EmailSchedule updated successfully!!"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            email_schedule = EmailTemplate.objects.get(pk=pk)
        except EmailTemplate.DoesNotExist:
            return Response({"error": "EmailSchedule not found"}, status=status.HTTP_404_NOT_FOUND)

        email_schedule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    


class EmailTemplateFormDataGet(APIView):
    def get(self, request, brand_id = None):
        if id is None:
            return Response({"error": "Method Not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            # Retrive Services
            services = Service.objects.filter(Brand_id=brand_id)  # Retrieve all instances of the Service model
            service_serializer = ServiceSerializer(services, many=True) 

            # Retrive Lead Scources Of the Given Brand
            leadScource = LeadSource.objects.filter(Brand = brand_id)
            lead_scource_serializer = LeadScourceSerializers(leadScource,many=True)

            # Email Templates
            email_template = EmailTemplate.objects.all()
            email_template_serializer = EmailTemplateSerializers(email_template, many=True)

            # Retrive Lead's
            if request.user.is_admin:
                lead_data = Lead.objects.all() 
            else:
                lead_data = Lead.objects.filter(LeadRep=request.user)  
            lead_data_serializer = LeadGetSerializer(lead_data, many= True)
            return Response({"services": service_serializer.data, "scource": lead_scource_serializer.data, "email_template": email_template_serializer.data, "lead_data": lead_data_serializer.data}, status=status.HTTP_200_OK)
            
