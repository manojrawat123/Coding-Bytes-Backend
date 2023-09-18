from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from paymentmode.serializers import PaymentModeSerializer
from myuser.renders import UserRenderer
from paymentmode.models import PaymentMode

# Create your views here.
class MyPaymentMode(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request,brand_id, format=None):
        payMode = PaymentMode.objects.filter(brand_id=brand_id)
        serializer = PaymentModeSerializer(payMode,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    
