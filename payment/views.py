from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from .models import Payment
from payment.serializers import PaymentSerializer
from django.db.models import Subquery
from feetracer.models import Fee


class PaymentList(APIView):
    def get(self, request, id=None):
        if id is None:
            payments = Payment.objects.all()
            serializer = PaymentSerializer(payments, many=True)
            return Response(serializer.data)
        elif id is not None:
            existing_payment_ids = Fee.objects.filter(payment_id__isnull=False).values_list('payment_id', flat=True)
            payments = Payment.objects.filter(lead_id=id).exclude(payment_id__in=existing_payment_ids)
            serializer = PaymentSerializer(payments, many=True)
            return Response(serializer.data)        

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PaymentByLead(APIView):
    def get(self, request, id =None):
        if id is not None:
            payments = Payment.objects.filter(lead_id= id)
            serializer = PaymentSerializer(payments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)  


class PaymentDetail(RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
