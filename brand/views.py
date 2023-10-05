from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from brand.models import Brand
from brand.serializers import BrandSerializers
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class BrandApiViewById(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id=None):
        if id is not None:
            brand = Brand.objects.get( id=id)
            serializers = BrandSerializers(brand)
            return Response(serializers.data,status= status.HTTP_200_OK) 
        return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)