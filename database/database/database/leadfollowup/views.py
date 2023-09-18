from django.shortcuts import render
from myuser.renders import UserRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from leadfollowup.models import LeadFollowUp
from leadfollowup.serializer import LeadFollowupSerializer

class LeadFollowupListCreateView(generics.ListCreateAPIView):
    # renderer_classes = [UserRenderer]
    # permission_classes = [IsAuthenticated]
    queryset = LeadFollowUp.objects.all()
    serializer_class = LeadFollowupSerializer

class LeadFollowupDetailView(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    queryset = LeadFollowUp.objects.all()
    serializer_class = LeadFollowupSerializer
