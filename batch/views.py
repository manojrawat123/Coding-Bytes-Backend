from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from batch.models import Batch
from batch.serializers import BatchSerializers
from rest_framework import status
from django.db.models import Q
from datetime import datetime, timedelta
from django.utils import timezone

# Create your views here.
class BatchApiView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        now = timezone.now().date()
        last_month = now - timedelta(days=30)
        to_date_pr = request.query_params.get('to_date', now)
        from_date_pr = request.query_params.get('from_date', last_month) 
        from_date = datetime.strptime(f"{to_date_pr}", "%Y-%m-%d").strftime("%Y-%m-%dT23:59:00Z")
        to_date = datetime.strptime(f"{from_date_pr}", "%Y-%m-%d").strftime("%Y-%m-%dT00:00:00Z") 

        
        batch = Batch.objects.filter(Q(BatchCreatedDate__lt = from_date) & Q(BatchCreatedDate__gt = to_date))  
        serializer = BatchSerializers(batch, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = BatchSerializers(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)



class BatchApiViewById(APIView):
    permission_classes = [IsAuthenticated]
    def put(self , request, id=None):
        batch = Batch.objects.get(BatchID = id)
        serializers = BatchSerializers(batch, data= request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

        