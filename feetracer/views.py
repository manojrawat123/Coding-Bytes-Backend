from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from feetracer.models import Fee
from feetracer.serializers import FeesSerializerGet, FeesSerializerPost
from rest_framework import generics
from django.db.models import Q
 


class FeeTrackerList(APIView):
    def get(self, request, id=None):
        if id is not None:
            customer = Fee.objects.filter(converted_id=id)
            serializer = FeesSerializerGet(customer, many=True)
            return Response(serializer.data)
        else:
            fee = Fee.objects.filter(representative=request.user)
            serializer = FeesSerializerGet(fee, many=True)
            return Response(serializer.data)
 
    def post(self, request):
        serializer = FeesSerializerPost(data=request.data)
        if serializer.is_valid():
            serializer.save()
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

