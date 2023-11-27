from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BatchStudent
from .serializers import BatchStudentSerializer,BatchStuByConvertedLead
from rest_framework.permissions import IsAuthenticated
from convertedstudent.models import convertedstudent
from convertedstudent.serializers import ConvertedStudentGetRealSerializer
from batch.models import Batch
from batch.serializers import BatchSerializers

class BatchStudentListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # Retrieve all BatchStudents
        batchstudent= BatchStudent.objects.all()
        serializer = BatchStudentSerializer(batchstudent, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Create a new BatchStudent
        serializer = BatchStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BatchStudentByConvertedIdView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id=None):
        if id is not None:
            try:
                batchStudent = BatchStudent.objects.get(ConvertedID=id)
                serializers = BatchStuByConvertedLead(batchStudent)
                return Response(serializers.data, status=status.HTTP_200_OK)
            except BatchStudent.DoesNotExist:
                return Response({'error': 'BatchStudent not found for the given ConvertedID'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id=None):
        if id is not None:
            try:
                batchstudent = BatchStudent.objects.get(ConvertedID=id)
                batchstudent.delete()
                return Response({'message': 'BatchStudent deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
            except BatchStudent.DoesNotExist:
                return Response({'error': 'BatchStudent not found'}, status=status.HTTP_404_NOT_FOUND)
            except BatchStudent.MultipleObjectsReturned:
                return Response({'error': 'Multiple BatchStudents found for the given ConvertedID'}, status=status.HTTP_400_BAD_REQUEST)


class BatchForConverted(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            convertLead = convertedstudent.objects.all()
            convert_lead_serializer = ConvertedStudentGetRealSerializer(convertLead, many=True)
            
            for i in convert_lead_serializer.data:
                try:
                    batchStudent = BatchStudent.objects.get(ConvertedID=i["ConvertedID"])
                    batch_student_serializers = BatchStuByConvertedLead(batchStudent)
                    i["assign_batch_details"] = batch_student_serializers.data                    
                except Exception as e:
                    i["assign_batch_details"] = None
            batch = Batch.objects.all() 
            batchserializer = BatchSerializers(batch, many=True)
            response_data = {"converted_data": convert_lead_serializer.data,"batch_data": batchserializer.data }
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"error": "Internal Server Error"}, status=status.HTTP_400_BAD_REQUEST)