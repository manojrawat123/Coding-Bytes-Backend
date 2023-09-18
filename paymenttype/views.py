from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from myuser.renders import UserRenderer
from paymenttype.models import PaymentType
from paymenttype.serializers import PaymentTypeSerializer

# Create your views here.
class MyPaymentType(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request,brand_id, format=None):
        payType = PaymentType.objects.filter(brand_id=brand_id)
        serializer = PaymentTypeSerializer(payType,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)