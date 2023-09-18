from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from navbar.models import MenuItem
from navbar.serializers import NavBarSerializer 

# Create your views here.
class MyNavbar(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, format=None):
        navbar = MenuItem.objects.all()
        serializer = NavBarSerializer(navbar,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)