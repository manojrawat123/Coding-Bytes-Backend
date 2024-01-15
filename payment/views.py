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
from messageshedule.views import send_sms
from emailshedule.views import custom_email_func
from convertedstudent.models import convertedstudent
from rest_framework.permissions import IsAuthenticated
from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models import Q


class PaymentList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id=None):
        if id is None:
            now = timezone.now().date()
            last_month = now - timedelta(days=30)
            
            to_date_pr = request.query_params.get('to_date', now)
            from_date_pr = request.query_params.get('from_date', last_month) 
            all_leads_params = request.query_params.get('all', None)  
            from_date = datetime.strptime(f"{to_date_pr}", "%Y-%m-%d").strftime("%Y-%m-%dT23:59:00Z")
            to_date = datetime.strptime(f"{from_date_pr}", "%Y-%m-%d").strftime("%Y-%m-%dT00:00:00Z")
            if request.user.is_admin:
                payments = Payment.objects.filter(Q(payment_date__lt = from_date) & Q(payment_date__gt = to_date))
            else:
                payments = Payment.objects.filter(Q(user_id = request.user) &Q(payment_date__lt = from_date) & Q(payment_date__gt = to_date))
            serializer = PaymentGetSerializers(payments, many=True)
            for i in serializer.data:
                try:
                    fees_data = Fee.objects.get(payment_id = i["payment_id"])
                    fees_serializer = FeesSerializerGet(fees_data)
                    i["fees_data"] = fees_serializer.data 
                except:
                    fees_data = None
                    i["fees_data"] = False
            return Response(serializer.data)
        elif id is not None:
            try:
                # This is when it is converted Id 
                # Fees All Data 
                fees_data = Fee.objects.filter(converted_id = id)
                fees_serializer = FeesSerializerPost(fees_data,many=True)

                # Done Payment 
                done_payment = sum(i.fee_received for i in fees_data)

                # Converted Data
                try:
                    converted_data = convertedstudent.objects.get(ConvertedID=id)
                except convertedstudent.DoesNotExist:
                    return Response({"error": "No Data Found"}, status=status.HTTP_404_NOT_FOUND)

                # Total & Pending Fees
                total_fees = converted_data.TotalFee
                pending_fees = total_fees - done_payment
                
                # lead & Payment Details
                lead_details = converted_data.LeadID
                lead_serializer = LeadGetSerializer(lead_details)
                existing_payment_id = fees_data.values_list('payment_id', flat=True)
                payment_details = Payment.objects.filter(lead_id = lead_details.id).exclude(payment_id__in= existing_payment_id)
                paymentserializer = PaymentGetSerializers(payment_details, many=True)
                return Response({
                    "payment_detail": paymentserializer.data ,
                        "done_payment": done_payment,
                        "pending_payment": pending_fees,
                        "total_fees": total_fees,
                        "lead_details": lead_serializer.data,
                        "feesDetails": fees_serializer.data
                    })
            except Exception as e:
                return Response({"error": "some error occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # send_sms(2, leadID = request.data.get("lead_id"), name= request.data.get("name"), phone=request.data.get("phone"), brandId=request.data.get("brand"), serviceId=request.data.get("payment_purpose"), companyId=request.data.get("company"),leadRepId=request.data.get("user_id")) 
            custom_email_func(6, addPayment = True, leadID = request.data.get("lead_id"), paymentId = serializer.data.get("payment_id"))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PaymentByLead(APIView):
    def get(self, request, id =None):
        if id is not None:
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
                    "total_fees": "",
                    "lead_details": lead_serializer.data,
                    "feesDetails": fees_serializer.data
                })


class PaymentDetail(RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
