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
# from convertedstudent.models import convertedstudent

class LeadFollowupListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id=None):
        if id is not None:
            customer = LeadFollowUp.objects.filter(Q(LeadID=id) & Q(LeadRep=request.user))
            
            serializer = LeadGetFollowUpSerializer(customer, many=True)
            return Response(serializer.data)
        
        else:
            fee = LeadFollowUp.objects.filter(LeadRep = request.user)
            serializer = LeadGetFollowUpSerializer(fee, many=True)
            return Response(serializer.data)
 
    def post(self, request):  
        try:
            leadFollowUpserializer = LeadFollowupSerializer(data=request.data)
            leadLastFollowUpserializer = LeadLastFollowUpSerializer(data = request.data)
            leadId = request.data.get("LeadID")
            serviceId = request.data.get("LeadServiceInterested")
            print("------")
            print(leadId)
            print(serviceId)
            leadStatus = request.data.get("LeadStatus")
            leadLastFollowUpData = LeadLastFollowUp.objects.get(LeadID=leadId, LeadServiceInterested=serviceId)

            
            
            leadData = Lead.objects.get(id = leadId)
            if leadData is None:
                return Response({"error": "Lead Id not exists"}, status=status.HTTP_400_BAD_REQUEST)
            leadSerializer = LeadSerializer(leadData, data={"LeadStatus": leadStatus}, partial=True)
            if leadLastFollowUpData is not None:
                leadLastFollowUpData.delete()
            
            if leadFollowUpserializer.is_valid() and leadLastFollowUpserializer.is_valid() and leadSerializer.is_valid():
                leadSerializer.save()
                leadLastFollowUpserializer.save()
                leadFollowUpserializer.save()
                return Response(leadFollowUpserializer.data, status=status.HTTP_201_CREATED)
            else:
                combined_errors = {
                    "leadFollowUp": leadFollowUpserializer.errors,
                    "leadLastFollowUp": leadLastFollowUpserializer.errors,
                    "lead": leadSerializer.errors,
                }
                return Response(combined_errors, status=status.HTTP_400_BAD_REQUEST)
                
        except Exception as e:
            print(f"ïnternal server error!! -- {e}")
            return Response({"Msg":"Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LeadFollowupDetailView(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    queryset = LeadFollowUp.objects.all()
    serializer_class = LeadFollowupSerializer
