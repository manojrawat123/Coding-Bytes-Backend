from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from service.models import Service
from service.serializers import ServiceSerializer
from myuser.renders import UserRenderer
from rest_framework.permissions import IsAuthenticated

class ServiceListView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request, brand_id, format=None):
        services = Service.objects.filter(Brand_id=brand_id)  # Retrieve all instances of the Service model
        serializer = ServiceSerializer(services, many=True)  # Serialize the queryset
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class ServiceListById(APIView):
    permission_classes = [IsAuthenticated]
    def get(self , request, id = None):
        if id == None:
            return Response({"Msg": "Registration Sucessfully!!"},status=status.HTTP_400_BAD_REQUEST)
        service = Service.objects.get(id = id)
        serializer = ServiceSerializer(service)
        return Response(serializer.data, status=status.HTTP_200_OK)
