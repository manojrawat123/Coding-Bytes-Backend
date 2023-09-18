from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from convertedstudent.models import convertedstudent
from convertedstudent.serializers import ConvertedStudentSerializer
from django.shortcuts import get_object_or_404

class ConvertedStudentList(APIView):
    def get(self, request, id=None):
        if id is not None:
            customer = convertedstudent.objects.filter(ConvertedID=id)
            serializer = ConvertedStudentSerializer(customer, many=True)
            return Response(serializer.data)
        
        else:
            customers = convertedstudent.objects.all()
            serializer = ConvertedStudentSerializer(customers, many=True)
            return Response(serializer.data)



    def post(self, request):
        serializer = ConvertedStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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

# class ConvertedStudentDetail(RetrieveAPIView):
#     queryset = convertedstudent.objects.all()
#     serializer_class = ConvertedStudentSerializer

