from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from convertedstudent.models import convertedstudent
from convertedstudent.serializers import ConvertedStudentSerializer, ConvertedStudentGetSerializer,ConvertedStudentGetRealSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Q
from customerstudent.serializers import CustomerSerializer
from feetracer.serializers import FeesSerializerPost
from lead.serializer import LeadSerializer, LeadGetSerializer
from lead.models import Lead
from feetracer.models import Fee
from payment.models import Payment
from emailshedule.views import custom_email_func 
from refundfees.models import FeeRefund

class ConvertedStudentList(APIView):
    def get(self, request, id=None):
        if id is not None:
            if request.user.is_admin:
                customer = convertedstudent.objects.filter(ConvertedID=id)
            else:
                customer = convertedstudent.objects.filter(Q(ConvertedId = id) & Q(Representative = request.user ))
            serializer = ConvertedStudentGetRealSerializer(customer, many=True)
            return Response(serializer.data)
        else:
            if request.user.is_admin:
                customers = convertedstudent.objects.all()
            else:
                customers = convertedstudent.objects.filter(Representative=request.user)
            serializer = ConvertedStudentGetRealSerializer(customers, many=True)
            return Response(serializer.data)


    def post(self, request):
        customerleadserializer = CustomerSerializer(data = request.data)

        if customerleadserializer.is_valid():
            customerleadserializer.save()
            # print("Customer Serializers success -: OK.")
        else:
            return Response(customerleadserializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        convertedData = {
                    "ClassMode": request.data.get("classMode"),
                    "CourseEndDate": request.data.get("courseEndDate"),
                    "CourseName": request.data.get("CourseName"),
                    "CourseStartDate": request.data.get("courseStartDate"),
                    "NextDueDate": request.data.get("nextDueDate"),
                    "PaymentID": request.data.get("payment_id"),
                    "Representative": request.data.get("clientRepresentative"),
                    "StudentID": customerleadserializer.data.get("CustomerID"),
                    "TotalFee": request.data.get("totalFee"),
                    "UpdateBY" :request.data.get("UpdateBY"), 
                }
        
        convertedserializer = ConvertedStudentSerializer(data={**request.data, **convertedData})
        if convertedserializer.is_valid():
            convertedserializer.save()
            # print("Converted Serializers success -: OK.")
        else: 
            return Response(convertedserializer.errors, status=status.HTTP_400_BAD_REQUEST)

        feesData = {
            "brand": request.data.get("Brand"),
            "company": request.data.get("Company"),
            "converted_id": convertedserializer.data.get("ConvertedID"),
            "lead": request.data.get("LeadID"),
            "representative": request.data.get("clientRepresentative"),
            "student": customerleadserializer.data.get("CustomerID"),
            "updated_by": request.data.get("UpdateBY") 
         }
        feeserializer = FeesSerializerPost(data={**request.data, **feesData})
        if feeserializer.is_valid():
            feeserializer.save()
        else:
            return Response(feeserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        LeadId = request.data.get("LeadID")
        leadData = Lead.objects.get(id = LeadId)
        leadSerializer = LeadSerializer(leadData, data={"LeadStatus": "Lead Converted"}, partial=True)
        if leadSerializer.is_valid():
            leadSerializer.save()
            custom_email_func(5, convertLead=True,leadID= request.data.get("LeadID"), studendtId=customerleadserializer.data.get("CustomerID"), convertedId=convertedserializer.data.get("ConvertedID"))
            return Response({"Msg": "Converted Sucessfully"})
        else:
            return Response(leadSerializer.errors, status=status.HTTP_400_BAD_REQUEST)





    def put(self, request, id=None):
        try:
            convertedStu = convertedstudent.objects.get(ConvertedID=id)
        except convertedstudent.DoesNotExist:
            return Response({"error": "Converted Student Id not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ConvertedStudentSerializer(convertedStu, data=request.data ,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# Pending Fees Details
class ConvertedStudentListWithFeesDetails(APIView):
    def get(self, request, id=None):
        if id != None:
            return Response({"error": "Method Not Allowed"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            if request.user.is_admin:
                myconvertedlist = convertedstudent.objects.all()
                convertedserializer = ConvertedStudentGetSerializer(myconvertedlist, many=True)
                for i in convertedserializer.data:
                    fees = Fee.objects.filter(lead = i["LeadID"])
                    payment_done = sum(i.fee_received for i in fees)
                    # print({i["LeadID"]:payment_done})
                    i["payment_done"] = payment_done
                    total_payment_arr = Payment.objects.filter(lead_id = i["LeadID"])
                    total_payment = int(float(i["TotalFee"]))                    
                    i["total_payment"] = total_payment
                    lost_payment =  float(i["LostSales"]) if i["LostSales"] is not None else 0
                    i["pending_fees"] = total_payment - payment_done - lost_payment
                    lead_obj = Lead.objects.get(id= i["LeadID"])
                    lead_serializer = LeadGetSerializer(lead_obj)
                    i["lead_obj"] = lead_serializer.data
                filtered_data = [item for item in convertedserializer.data if item.get('pending_fees', 0) != 0]
                return Response(filtered_data)
            else:
                myconvertedlist = convertedstudent.objects.filter(Representative = request.user)
                convertedserializer = ConvertedStudentGetSerializer(myconvertedlist, many=True)
                for i in convertedserializer.data:
                    fees = Fee.objects.filter(lead = i["LeadID"])
                    payment_done = sum(i.fee_received for i in fees)
                    # print({i["LeadID"]:payment_done})
                    i["payment_done"] = payment_done
                    total_payment = int(float(i["TotalFee"]))
                    i["total_payment"] = total_payment
                    lost_payment = float(i["LostSales"]) if i["LostSales"] is not None else 0

                    i["pending_fees"] = total_payment - payment_done - lost_payment
                    lead_obj = Lead.objects.get(id= i["LeadID"])
                    lead_serializer = LeadGetSerializer(lead_obj)
                    i["lead_obj"] = lead_serializer.data
                filtered_data = [item for item in convertedserializer.data if item.get('pending_fees', 0) != 0]
                return Response(filtered_data)

class RegisterdStudentDetails(APIView):
    def get(self, request, id=None):
        if id is not None:
            return Response({"error": "method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            if request.user.is_admin:
                myconvertedlist = convertedstudent.objects.all()
                convertedserializer = ConvertedStudentGetSerializer(myconvertedlist, many=True)
                for i in convertedserializer.data:
                    fees = Fee.objects.filter(lead = i["LeadID"])
                    payment_done = sum(i.fee_received for i in fees)
                    # print({i["LeadID"]:payment_done})
                    i["payment_done"] = payment_done
                    total_payment_arr = Payment.objects.filter(lead_id = i["LeadID"])
                    total_payment = int(float(i["TotalFee"]))                    
                    i["total_payment"] = total_payment
                    i["pending_fees"] = total_payment - payment_done
                    refund_fees = FeeRefund.objects.filter(ConvertedID = i["ConvertedID"])
                    if len(refund_fees) == 0:
                        i["fees_refund"] = 0
                    else:
                        i["fees_refund"] = sum(i.FeeRefunded for i in refund_fees)

                    lead_obj = Lead.objects.get(id= i["LeadID"])
                    lead_serializer = LeadGetSerializer(lead_obj)
                    i["lead_obj"] = lead_serializer.data
                return Response(convertedserializer.data)
            else:
                myconvertedlist = convertedstudent.objects.filter(Representative = request.user)
                convertedserializer = ConvertedStudentGetSerializer(myconvertedlist, many=True)
                for i in convertedserializer.data:
                    fees = Fee.objects.filter(lead = i["LeadID"])
                    payment_done = sum(i.fee_received for i in fees)
                    # print({i["LeadID"]:payment_done})
                    i["payment_done"] = payment_done
                    total_payment = int(float(i["TotalFee"]))
                    i["total_payment"] = total_payment
                    i["pending_fees"] = total_payment - payment_done
                    
                    refund_fees = FeeRefund.objects.filter(ConvertedID = i["ConvertedID"])
                    if len(refund_fees) == 0:
                        i["fees_refund"] = 0
                    else:
                        i["fees_refund"] = sum(i.FeeRefunded for i in refund_fees)
                    lead_obj = Lead.objects.get(id= i["LeadID"])
                    lead_serializer = LeadGetSerializer(lead_obj)
                    i["lead_obj"] = lead_serializer.data
                return Response(convertedserializer.data)