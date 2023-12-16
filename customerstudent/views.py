from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from customerstudent.models import Customer
from customerstudent.serializers import CustomerSerializer, CustomerGetSerializer
from django.db.models import Q
from convertedstudent.models import convertedstudent
from feetracer.models import Fee
from feetracer.serializers import FeesSerializerGet
from messagelog.models import MessageLog
from messagelog.serializers import MessageLogSerializer
from leadfollowup.models import LeadFollowUp
from leadfollowup.serializer import LeadFollowupSerializer,LeadGetFollowUpSerializer
from rest_framework.permissions import IsAuthenticated
from convertedstudent.serializers import ConvertedStudentGetRealSerializer

class CustomerList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id=None):
        if id is not None:
            # Converted Details
            try:
                if request.user.is_admin:
                    converted_detail = convertedstudent.objects.get(ConvertedID = id)
                    converted_serializer = ConvertedStudentGetRealSerializer(converted_detail)
                else:    
                    converted_detail = convertedstudent.objects.get(Q(ConvertedID = id) & Q(Representative = request.user))
                    converted_serializer = ConvertedStudentGetRealSerializer(converted_detail)
            except Exception as e:
                print("some Error occured")
                print(e)
                return Response({"error": "No Data"},status=status.HTTP_404_NOT_FOUND)
            
            # Lead Id 
            lead_id = converted_detail.LeadID.id 
            message_details = MessageLog.objects.filter(LeadId = lead_id)
            message_serializer = MessageLogSerializer(message_details, many=True)
            
            # Fees Details
            fees_details = Fee.objects.filter(converted_id = id)
            fees_serializer = FeesSerializerGet(fees_details, many=True)

            # Lead FollowUp
            lead_follow_up_details = LeadFollowUp.objects.filter(LeadID=lead_id)
            lead_follow_up_serializer = LeadGetFollowUpSerializer(lead_follow_up_details, many=True)
 
            return Response({"converted_data": converted_serializer.data, "fees_details": fees_serializer.data, "message_log":message_serializer.data, "lead_follow_up_details":lead_follow_up_serializer.data})

        else:
            print("hii")
            if request.user.is_admin:
                converted_detail = convertedstudent.objects.all()
            else:
                converted_detail = convertedstudent.objects.filter(Representative = request.user)                
            customer_serializer = ConvertedStudentGetRealSerializer(converted_detail,many=True)
            return Response(customer_serializer.data, status=status.HTTP_200_OK)

            
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id=None):
        if id is None:
            return Response({"error": "Method Not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            try:

                customerStu = Customer.objects.get(CustomerID = id)
            except customerStu.DoesNotExist:
                return Response({"error": "Customer Student Id Does not exists"}, status=status.HTTP_404_NOT_FOUND)
            serializer = CustomerSerializer(customerStu, data=request.data , partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)






class CustomerDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id = None):
        if id is not None:
            customer = Customer.objects.get(CustomerID = id)
            customer_serializer = CustomerGetSerializer(customer)
            return Response(customer_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Some Error Occured"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            
