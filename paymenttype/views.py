from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from myuser.renders import UserRenderer
from paymenttype.models import PaymentType
from paymenttype.serializers import PaymentTypeSerializer
from leadScource.models import LeadSource
from leadScource.serializers import LeadScourceSerializers
from paymentmode.serializers import PaymentModeSerializer
from paymentmode.models import PaymentMode
from service.models import Service
from service.serializers import ServiceSerializer 

# Create your views here.
class MyPaymentType(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request,brand_id, format=None):
        payType = PaymentType.objects.filter(brand_id=brand_id)
        serializer = PaymentTypeSerializer(payType,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class PaymentModeTypeService(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, brand_id = None):
        if id is None:
            return Response({"error": "Method Not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            # Lead Scource
            lead_scource = LeadSource.objects.filter(Brand = brand_id)
            lead_scource_serializer = LeadScourceSerializers(lead_scource, many=True)

            # Payment Mode
            payment_mode = PaymentMode.objects.filter(brand = brand_id)
            payment_mode_serializer = PaymentModeSerializer(payment_mode, many=True)

            # Payment Type
            payment_type = PaymentType.objects.filter(brand_id=brand_id)
            payment_type_serializer = PaymentTypeSerializer(payment_type, many=True)

            # Service 
            service_data = Service.objects.filter(Brand = brand_id)
            service_serializer = ServiceSerializer(service_data, many=True)

            return Response({ 
                            "lead_scource":lead_scource_serializer.data, 
                            "payment_type": payment_type_serializer.data,
                            "payment_mode":payment_mode_serializer.data,
                            "service": service_serializer.data
                        }, status=status.HTTP_200_OK)
            