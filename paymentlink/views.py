from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from paymentlink.models import PaymentLink
from paymentlink.serializers import PaymentLinkSerializers
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class PaymentLinkView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, format=None):
        paymentlink = PaymentLink.objects.all()
        serializers = PaymentLinkSerializers(paymentlink, many=True)
        return Response(serializers.data, status = status.HTTP_200_OK)
    


    def post(self, request):
        serializers = PaymentLinkSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status= status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Create your views here.
class PaymentLinkViewGetUrl(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        url = request.GET.get('url')  # Get the URL from the query parameters

        try:
            paymentlink = PaymentLink.objects.get(PaymentLink=url)
            serializer = PaymentLinkSerializers(paymentlink)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PaymentLink.DoesNotExist:
            return Response({'error': 'PaymentLink not found for the given URL.'}, status=status.HTTP_404_NOT_FOUND)
