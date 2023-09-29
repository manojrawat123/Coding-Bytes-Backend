from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from refundfees.models import FeeRefund
from refundfees.serializers import RefundFeesSerializer

class FeesRefundApiView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, id=None):
        if id is not None:
            customer = FeeRefund.objects.filter(LeadID=id)
            serializer = RefundFeesSerializer(customer, many=True)
            return Response(serializer.data)
        else:
            fee = FeeRefund.objects.all()
            serializer = RefundFeesSerializer(fee, many=True)
            return Response(serializer.data)
 
    def post(self, request):
        serializer = RefundFeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
