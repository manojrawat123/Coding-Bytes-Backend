from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from leadScource.models import LeadSource
from leadScource.serializers import LeadScourceSerializers


# Create your views here.
class LeadScourceApiView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, format=None):
        navbar = LeadSource.objects.all()
        serializer = LeadScourceSerializers(navbar,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LeadScourceApiById(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, format=None, id = None):
        if (id == None): 
            return Response({"msg":"method not allowed"})
        navbar = LeadSource.objects.filter(Brand = id)
        serializer = LeadScourceSerializers(navbar,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



