from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BatchStudent
from .serializers import BatchStudentSerializer,BatchStuByConvertedLead
from rest_framework.permissions import IsAuthenticated

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
