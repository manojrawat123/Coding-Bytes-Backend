from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from feetracer.models import Fee
from feetracer.serializers import FeesSerializerGet, FeesSerializerPost
from rest_framework import generics
from django.db.models import Q
from emailshedule.views import custom_email_func
from datetime import datetime, timedelta
from django.utils import timezone


class FeeTrackerList(APIView):
    def get(self, request, id=None):
        if id is not None:
            
            customer = Fee.objects.filter(Q(representative=request.user) & Q(converted_id=id))
            serializer = FeesSerializerGet(customer, many=True)
            return Response(serializer.data)
        else:
            now = timezone.now().date()
            last_month = now - timedelta(days=30)
            to_date_pr = request.query_params.get('to_date', now)
            from_date_pr = request.query_params.get('from_date', last_month) 
            from_date = datetime.strptime(f"{to_date_pr}", "%Y-%m-%d").strftime("%Y-%m-%dT23:59:00Z")
            to_date = datetime.strptime(f"{from_date_pr}", "%Y-%m-%d").strftime("%Y-%m-%dT00:00:00Z")  
            if request.user.is_admin:
                fee = Fee.objects.filter(Q(fee_created_datetime__lt = from_date) & Q(fee_created_datetime__gt = to_date))
            else:
                fee = Fee.objects.filter(Q(representative=request.user) & Q(fee_created_datetime__lt = from_date) & Q(fee_created_datetime__gt = to_date))
            serializer = FeesSerializerGet(fee, many=True)
            for i in serializer.data:
                fees_data_student = Fee.objects.filter(converted_id = i["converted_id"]["ConvertedID"]).values_list("fee_received", flat=True)
                paid_fees = sum(i for i in fees_data_student)
                i["paid_fees"] = paid_fees
            return Response(serializer.data)
 
    def post(self, request):
        serializer = FeesSerializerPost(data=request.data)
        if serializer.is_valid():
            serializer.save()
            custom_email_func(3, addPendingFees=True, leadID= request.data.get("lead"), feesID=serializer.data.get("id"))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, id=None):
        try:
            fee = Fee.objects.get(id=id)
        except Fee.DoesNotExist:
            return Response({"error": "Fee not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = FeesSerializerPost(fee, data=request.data ,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeeTracerByPaymentID(APIView):
    def get(self, request, id=None):
        if id is not None:
            customer = Fee.objects.filter(payment_id=id)
            serializer = FeesSerializerGet(customer, many=True)
            return Response(serializer.data)
        else:
            fee = Fee.objects.all()
            serializer = FeesSerializerGet(fee, many=True)
            return Response(serializer.data)      

class FeeTrackekrkDetail(generics.ListCreateAPIView):
    queryset = Fee.objects.all()
    serializer_class = FeesSerializerPost