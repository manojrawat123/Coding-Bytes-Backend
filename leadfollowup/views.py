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
from datetime import datetime, timedelta
from django.utils import timezone

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
            now = timezone.now().date()
            last_month = now - timedelta(days=30)
            
            to_date_pr = request.query_params.get('to_date', now)
            from_date_pr = request.query_params.get('from_date', last_month) 
            follow_status = request.query_params.get('follow_up_status', "all")
            from_date = datetime.strptime(f"{to_date_pr}", "%Y-%m-%d").strftime("%Y-%m-%dT23:59:00Z")
            to_date = datetime.strptime(f"{from_date_pr}", "%Y-%m-%d").strftime("%Y-%m-%dT00:00:00Z")


    
            if request.query_params.get("follow_up_status") == "all":
                if request.user.is_admin:
                    leadfollowup = LeadFollowUp.objects.filter(Q(LeadStatusDate__lt = from_date) & Q(LeadStatusDate__gt = to_date))
                else:
                    leadfollowup = LeadFollowUp.objects.filter(Q(LeadRep = request.user) & Q(LeadStatusDate__lt = from_date) & Q(LeadStatusDate__gt = to_date))
            else:
                if request.user.is_admin:
                    print(follow_status)
                    leadfollowup = LeadFollowUp.objects.filter(Q(LeadStatusDate__lt = from_date) & Q(LeadStatusDate__gt = to_date) & Q(LeadStatus = follow_status))
                else:
                    leadfollowup = LeadFollowUp.objects.filter(Q(LeadRep = request.user) & Q(LeadStatusDate__lt = from_date) & Q(LeadStatusDate__gt = to_date) & Q(LeadStatus = follow_status))
                
                
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
                print("debug 1")
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

class LeadAnalystView(APIView):
    def get(self, request, id=None):
        if id is not None:
            return Response({"error": "method Not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            now = timezone.now().date()
            last_month = now - timedelta(days=30)
            
            to_date_pr = request.query_params.get('to_date', now)
            from_date_pr = request.query_params.get('from_date', last_month) 
            all_leads_params = request.query_params.get('all', None)  
            from_date = datetime.strptime(f"{to_date_pr}", "%Y-%m-%d").strftime("%Y-%m-%dT23:59:00Z")
            to_date = datetime.strptime(f"{from_date_pr}", "%Y-%m-%d").strftime("%Y-%m-%dT00:00:00Z") 


            if request.user.is_admin:
                # lead_analyst = LeadFollowUp.objects.all()
                lead_analyst = LeadFollowUp.objects.filter(Q(LeadStatusDate__lt = from_date) & Q(LeadStatusDate__gt = to_date)) 
            else:
                lead_analyst = LeadFollowUp.objects.filter(Q(LeadRepresentativePrimary=request.user) & Q(LeadStatusDate__lt = from_date) & Q(LeadStatusDate__gt = to_date)) 
            lead_analyst_serializer = LeadGetFollowUpSerializer(lead_analyst, many=True)

            return Response(lead_analyst_serializer.data, status=status.HTTP_200_OK) 
