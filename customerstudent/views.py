from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from customerstudent.models import Customer
from customerstudent.serializers import CustomerSerializer

class CustomerList(APIView):
    def get(self, request):
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id=None):
        try:
            customerStu = Customer.objects.get(CustomerId = id)
        except customerStu.DoesNotExist:
            return Response({"error": "Customer Student Id Does not exists"})
        serializer = CustomerSerializer(customerStu, data=request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)




class CustomerDetail(RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
