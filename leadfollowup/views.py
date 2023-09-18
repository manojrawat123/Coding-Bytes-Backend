from django.shortcuts import render
from myuser.renders import UserRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from leadfollowup.models import LeadFollowUp
from leadfollowup.serializer import LeadFollowupSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class LeadFollowupListCreateView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, id=None):
        if id is not None:
            customer = LeadFollowUp.objects.filter(LeadID=id)
            serializer = LeadFollowupSerializer(customer, many=True)
            return Response(serializer.data)
        else:
            fee = LeadFollowUp.objects.all()
            serializer = LeadFollowupSerializer(fee, many=True)
            return Response(serializer.data)
 
    def post(self, request):
        serializer = LeadFollowupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LeadFollowupDetailView(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    queryset = LeadFollowUp.objects.all()
    serializer_class = LeadFollowupSerializer
