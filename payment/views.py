from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from .models import Payment
from payment.serializers import PaymentSerializer,PaymentGetSerializers
from django.db.models import Subquery
from feetracer.models import Fee
from django.db.models import Sum
from lead.models import Lead
from lead.serializer import LeadGetSerializer
from feetracer.serializers import FeesSerializerGet, FeesSerializerPost

class PaymentList(APIView):
    def get(self, request, id=None):
        if id is None:
            payments = Payment.objects.all()
            serializer = PaymentGetSerializers(payments, many=True)
            for i in serializer.data:
                try:
                    fees_data = Fee.objects.get(payment_id = i["payment_id"])
                    fees_serializer = FeesSerializerGet(fees_data)
                    i["fees_data"] = fees_serializer.data 
                except:
                    fees_data = None
                    i["fees_data"] = False
                print({i["payment_id"]: fees_data})
            return Response(serializer.data)
        elif id is not None:
            existing_payment_ids = Fee.objects.filter(payment_id__isnull=False).values_list('payment_id', flat=True)
            payments = Payment.objects.filter(lead_id=id).exclude(payment_id__in=existing_payment_ids)
            payments_done = Payment.objects.filter(lead_id=id, payment_id__in=existing_payment_ids)
            fees_data = Fee.objects.filter(lead =id)
            fees_serializer = FeesSerializerPost(fees_data,many=True)
            done_payment = sum(i.payment_amount for i in payments_done)
            lead_details = Lead.objects.get(id=id)
            lead_serializer = LeadGetSerializer(lead_details)
            pending_payment = sum(i.payment_amount for i in payments)
            paymentserializer = PaymentGetSerializers(payments, many=True)
            return Response({"payment_detail": paymentserializer.data ,
                    "done_payment": done_payment,
                    "pending_payment": pending_payment,
                    "lead_details": lead_serializer.data,
                    "feesDetails": fees_serializer.data
                })

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
            serializer = PaymentGetSerializers(payments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)  


class PaymentDetail(RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
