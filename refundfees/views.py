from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from refundfees.models import FeeRefund
from refundfees.serializers import RefundFeesSerializer
from paymenttype.models import PaymentType
from paymenttype.serializers import PaymentTypeSerializer
from leadScource.models import LeadSource
from leadScource.serializers import LeadScourceSerializers
from paymentmode.serializers import PaymentModeSerializer
from paymentmode.models import PaymentMode
from service.models import Service
from service.serializers import ServiceSerializer 
from convertedstudent.models import convertedstudent
from convertedstudent.serializers import ConvertedStudentGetRealSerializer 
from feetracer.models import Fee
from lead.serializer import LeadGetSerializer
# from feetracer.serializers import FeesSerializerGet

class FeesRefundApiView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id=None):
        if id is not None:
            customer = FeeRefund.objects.filter(LeadID=id )
            serializer = RefundFeesSerializer(customer, many=True)
            return Response(serializer.data)
        else:
            if request.user.is_admin:
                fee_refund = FeeRefund.objects.all()
            else:
                fee_refund = FeeRefund.objects.filter(Representative = request.user)
            serializer = RefundFeesSerializer(fee_refund, many=True)
            for i in serializer.data:
                fees_data = Fee.objects.filter(converted_id = i["ConvertedID"])   
                converted_obj = convertedstudent.objects.get(ConvertedID = i["ConvertedID"])             
                total_payment = converted_obj.TotalFee
                done_payment = sum(i.fee_received for i in fees_data)
                pending_fees = total_payment - done_payment
                i["payment_done"] = done_payment
                i["pending_fees"] = pending_fees
                i["total_fees"] = total_payment
                
                i["lead_obj"] = LeadGetSerializer(converted_obj.LeadID).data  
                
            return Response(serializer.data)
 
    def post(self, request):
        serializer = RefundFeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class FeesRefundPageDisplayView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, brand_id = None, convert_id= None):
        if brand_id | convert_id is None:
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

            # Payment Done
            fees_data = Fee.objects.filter(converted_id = convert_id)
            done_payment = sum(i.fee_received for i in fees_data)

            # Refund Fees
            refund_fees_data = FeeRefund.objects.filter(ConvertedID = convert_id)
            refund_fees = sum(i.FeeRefunded for i in refund_fees_data)
            done_payment_minus_refund = done_payment - refund_fees

            # Converted Data
            try:
                converted_data = convertedstudent.objects.get(ConvertedID = convert_id)
                converted_data_serializer = ConvertedStudentGetRealSerializer(converted_data)
            except Exception as e:
                return Response({"error": "No Data is found"}, status=status.HTTP_404_NOT_FOUND)            
            return Response({ 
                            "lead_scource":lead_scource_serializer.data, 
                            "payment_type": payment_type_serializer.data,
                            "payment_mode":payment_mode_serializer.data,
                            "service": service_serializer.data,
                            "converted_data": converted_data_serializer.data,
                            "payment_done": done_payment_minus_refund,
                        }, status=status.HTTP_200_OK)