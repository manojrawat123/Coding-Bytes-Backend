from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from service.models import Service
from .serializers import LeadSerializer
from myuser.renders import UserRenderer
from rest_framework.permissions import IsAuthenticated

class ServiceListView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        services = Service.objects.all()  # Retrieve all instances of the Service model
        serializer = LeadSerializer(services, many=True)  # Serialize the queryset
        
        return Response(serializer.data, status=status.HTTP_200_OK)
