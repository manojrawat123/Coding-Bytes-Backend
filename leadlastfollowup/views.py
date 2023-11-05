from django.shortcuts import render
from myuser.renders import UserRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from leadlastfollowup.models import LeadLastFollowUp
from leadlastfollowup.serializer import LeadLastFollowUpSerializer
from django.http import JsonResponse
from lead.models import Lead
from rest_framework.response import Response
from rest_framework.views import APIView
from convertedstudent.models import convertedstudent
from rest_framework import status


class LeadLastFollowupListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = LeadLastFollowUp.objects.all()
    serializer_class = LeadLastFollowUpSerializer
     

class LeadLastFollowUpByLeadId(APIView):
    def get(self, request, id=None):
        if id is not None:
            customer = LeadLastFollowUp.objects.filter(LeadID=id)
            serializer = LeadLastFollowUpSerializer(customer, many=True)
            return Response(serializer.data)
        else:
            fee = LeadLastFollowUp.objects.all()
            serializer = LeadLastFollowUpSerializer(fee, many=True)
            return Response(serializer.data)
        
    def post(self, request, id = None):
        if id is None:
            
            return Response({"error": "Method Not Allowed!!"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            customer = LeadLastFollowUp.objects.get(LeadID=id)
            # Delete the existing customer object
            customer.delete()
            
            # Create a new customer object with the new data
            serializer = LeadLastFollowUpSerializer(data=request.data)
        except LeadLastFollowUp.DoesNotExist:
            # The customer with the specified LeadID doesn't exist, create a new one
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

        serializer = LeadLastFollowUpSerializer(sorted_followups, many=True)

        return Response(serializer.data)