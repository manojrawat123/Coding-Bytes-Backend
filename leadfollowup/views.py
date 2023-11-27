from django.shortcuts import render
from myuser.renders import UserRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from leadfollowup.models import LeadFollowUp
from leadfollowup.serializer import LeadFollowupSerializer,LeadGetFollowUpSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from leadlastfollowup.serializer import LeadLastFollowUpSerializer
from leadlastfollowup.models import LeadLastFollowUp
from lead.models import Lead
from lead.serializer import LeadSerializer
from service.models import Service
from service.serializers import ServiceSerializer
# from convertedstudent.models import convertedstudent

class LeadFollowupListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id=None):
        if id is not None:
            customer = LeadFollowUp.objects.filter(Q(LeadID=id) & Q(LeadRep=request.user))

            serializer = LeadGetFollowUpSerializer(customer, many=True)
            for i in serializer.data:
                lead_id = i["LeadID"]
                lead_service_interested_objects = lead_id["LeadServiceInterested"]
                lead_service_interested_ids = [item["id"] for item in lead_service_interested_objects]
                avaible_services = Service.objects.exclude(id__in=lead_service_interested_ids)
                services_serializer = ServiceSerializer(avaible_services, many=True)
                i["available_services"] = services_serializer.data

            return Response(serializer.data)
        
        else:
            leadfollowup = LeadFollowUp.objects.filter(LeadRep = request.user)
            serializer = LeadGetFollowUpSerializer(leadfollowup, many=True)
            return Response(serializer.data)
 
    def post(self, request):  
        try:
            leadFollowUpserializer = LeadFollowupSerializer(data=request.data)
            leadLastFollowUpserializer = LeadLastFollowUpSerializer(data = request.data)
            leadId = request.data.get("LeadID")
            serviceId = request.data.get("LeadServiceInterested")
            leadStatus = request.data.get("LeadStatus")
            leadData = Lead.objects.get(id = leadId)
            if leadData is None:
                return Response({"error": "Lead Id not exists"}, status=status.HTTP_400_BAD_REQUEST)
            leadSerializer = LeadSerializer(leadData, data={"LeadStatus": leadStatus}, partial=True)
            
            
            if leadFollowUpserializer.is_valid():
                leadFollowUpserializer.save()
            else:
                return Response(leadFollowUpserializer.errors,status=status.HTTP_400_BAD_REQUEST)
            if leadLastFollowUpserializer.is_valid():
                try:
                    leadLastFollowUpData = LeadLastFollowUp.objects.get(Q(LeadID=leadId) &  Q(LeadServiceInterested=serviceId))
                    if leadLastFollowUpData is not None:
                        leadLastFollowUpserializer.save()
                        leadLastFollowUpData.delete()
                except:
                    print("Data Not Found")
                    return Response({"error": "Service Not match"}, status=status.HTTP_400_BAD_REQUEST)
                
            else:
                return Response(leadLastFollowUpserializer.errors,status=status.HTTP_400_BAD_REQUEST)
            if leadSerializer.is_valid():
                leadSerializer.save()
                return Response({"Sucess": "Data Submitted Sucessfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response(leadSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
        except Exception as e:
            print(f"ïnternal server error!! -- {e}")
            return Response({"Msg":"Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LeadFollowupDetailView(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    queryset = LeadFollowUp.objects.all()
    serializer_class = LeadFollowupSerializer
