from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from convertedstudent.models import convertedstudent
from convertedstudent.serializers import ConvertedStudentSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Q
from customerstudent.serializers import CustomerSerializer
from feetracer.serializers import FeesSerializerPost
from lead.serializer import LeadSerializer
from lead.models import Lead

class ConvertedStudentList(APIView):
    def get(self, request, id=None):
        if id is not None:
            if request.user.is_admin:
                customer = convertedstudent.objects.filter(ConvertedID=id)
            else:
                customer = convertedstudent.objects.filter(Q(ConvertedId = id) & Q(Representative = request.user ))
            serializer = ConvertedStudentSerializer(customer, many=True)
            return Response(serializer.data)
        else:
            if request.user.is_superuser:
                customers = convertedstudent.objects.all()
            else:
                customers = convertedstudent.objects.filter(Representative=request.user)
            serializer = ConvertedStudentSerializer(customers, many=True)
            return Response(serializer.data)



    def post(self, request):
        customerleadserializer = CustomerSerializer(data = request.data)

        if customerleadserializer.is_valid():
            customerleadserializer.save()
            print("Customer Serializers success -: OK.")
        else:
            return Response(customerleadserializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            
        convertedData = {
                    "ClassMode": request.data.get("classMode"),
                    "CourseEndDate": request.data.get("courseEndDate"),
                    "CourseName": request.data.get("package"),
                    "CourseStartDate": request.data.get("courseStartDate"),
                    "NextDueDate": request.data.get("nextDueDate"),
                    "PaymentID": request.data.get("payment_id"),
                    "Representative": request.data.get("clientRepresentative"),
                    "StudentID": customerleadserializer.data.get("CustomerID"),
                    "TotalFee": request.data.get("totalFee"),
                    "UpdateBY" :request.data.get("UpdateBY") 
                }
        
        convertedserializer = ConvertedStudentSerializer(data={**request.data, **convertedData})
        if convertedserializer.is_valid():
            convertedserializer.save()
            print("Converted Serializers success -: OK.")
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
            print("Fees Serializers success -: OK.")
        else:
            return Response(feeserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        LeadId = request.data.get("LeadID")
        leadData = Lead.objects.get(id = LeadId)
        leadSerializer = LeadSerializer(leadData, data={"LeadStatus": "Lead Converted"}, partial=True)
        if leadSerializer.is_valid():
            leadSerializer.save()
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