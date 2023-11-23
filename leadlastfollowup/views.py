from django.shortcuts import render
from myuser.renders import UserRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from leadlastfollowup.models import LeadLastFollowUp
from leadlastfollowup.serializer import LeadLastFollowUpSerializer, LeadLastFollowupGetSerializer
from django.http import JsonResponse
from lead.models import Lead
from rest_framework.response import Response
from rest_framework.views import APIView
from convertedstudent.models import convertedstudent
from rest_framework import status
from django.db.models import Q



class LeadLastFollowupListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = LeadLastFollowUp.objects.all()
    serializer_class = LeadLastFollowUpSerializer
     

class LeadLastFollowUpByLeadId(APIView):
    def get(self, request, id=None):
        if id is not None:
            customer = LeadLastFollowUp.objects.filter(LeadID=id)
            serializer = LeadLastFollowupGetSerializer(customer, many=True)
            return Response(serializer.data)
        else:
            lastfollowup = LeadLastFollowUp.objects.all()
            serializer = LeadLastFollowupGetSerializer(lastfollowup, many=True)
            return Response(serializer.data)
        
    def post(self, request, id = None):
        if id is None:
            return Response({"error": "Method Not Allowed!!"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            serviceId = request.data.get('LeadServiceInterested')
            customer = LeadLastFollowUp.objects.get(Q(LeadID=id) & Q(LeadServiceInterested=serviceId))
            print(customer)
            customer.delete()
            serializer = LeadLastFollowUpSerializer(data=request.data)
        except LeadLastFollowUp.DoesNotExist:
            serializer = LeadLastFollowUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Msg": "Updated Successfully!!"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 



class LeadLastFollowUpNotConverted(APIView):

    def get(self, request):
        status_order = {
            'Fresh': 1,'Ready To Enroll': 2,'Visit scheduled': 3,'Demo scheduled': 4,"Highly Intersted": 5,"Least Intersted": 6,"Distance Issue": 7,"Pricing Issue": 8,"Already Taken Service": 9,"Quality Issue": 10,"Not Interested Anymore": 11,"Did Not Enquire": 12,"Only Wanted Information": 13,"Other": 14,
        }
        followups_not_converted = LeadLastFollowUp.objects.exclude(LeadID__in=convertedstudent.objects.values('LeadID'))

        sorted_followups = sorted(followups_not_converted, key=lambda x: status_order.get(x.LeadStatus, float('inf')))

        serializer = LeadLastFollowupGetSerializer(sorted_followups, many=True)

        return Response(serializer.data)