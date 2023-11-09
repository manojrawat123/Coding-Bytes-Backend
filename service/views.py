from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from service.models import Service
from django.http import JsonResponse
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
            return Response({"Msg": "Bad Request!!"},status=status.HTTP_400_BAD_REQUEST)
        service = Service.objects.get(id = id)
        serializer = ServiceSerializer(service)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetServiceDetailsArrByID(APIView):
    def get(self, request):
        try:
            ids_param = request.query_params.get('ids', '')
            ids = [int(id) for id in ids_param.split(',') if id.isdigit()]
            print(ids)
        except (ValueError, AttributeError) as e:
            return Response({'error': 'Invalid ID format'}, status=status.HTTP_400_BAD_REQUEST)
        services = Service.objects.filter(id__in=ids)
        service_serializer = ServiceSerializer(services, many=True)
        return Response({'services': service_serializer.data}, status=status.HTTP_200_OK)





