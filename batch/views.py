from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from batch.models import Batch
from batch.serializers import BatchSerializers
from rest_framework import status


# Create your views here.
class BatchApiView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        batch = Batch.objects.all() 
        serializer = BatchSerializers(batch, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = BatchSerializers(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

        