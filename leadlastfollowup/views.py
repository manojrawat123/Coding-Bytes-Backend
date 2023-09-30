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


class LeadLastFollowupListCreateView(generics.ListCreateAPIView):
    # renderer_classes = [UserRenderer]
    # permission_classes = [IsAuthenticated]
    queryset = LeadLastFollowUp.objects.all()
    serializer_class = LeadLastFollowUpSerializer
    
                       
    # def post(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.POST)
    #     serializer.is_valid(raise_exception=True)
    #     lead_last_followup = serializer.save()

    # # Update the foreign key with the new value from the POST request
    #     if lead_last_followup.LeadID is not None:
    #         lead = Lead.objects.get(pk=lead_last_followup.LeadID)
    #         lead.LeadID = serializer.validated_data['LeadID']
    #         lead.save()

    #     return JsonResponse({'success': True})

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

class LeadLastFollowupDetailView(generics.RetrieveUpdateDestroyAPIView):

    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    queryset = LeadLastFollowUp.objects.all()
    serializer_class = LeadLastFollowUpSerializer
    def put(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        lead_last_followup = LeadLastFollowUp.objects.get(pk=pk)
        serializer = self.serializer_class(lead_last_followup, data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    # Update the foreign key with the new value from the POST request
        if serializer.validated_data['LeadID'] is not None:
            lead_last_followup.LeadID = serializer.validated_data['LeadID']
            lead_last_followup.save()

        return JsonResponse({'success': True})