from django.shortcuts import render
from rest_framework.views import APIView
from myuser.renders import UserRenderer
from lead.serializer import LeadSerializer,LeadGetSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated
from lead.models import Lead
from rest_framework.generics import RetrieveAPIView
from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from leadfollowup.serializer import LeadFollowupSerializer
from leadlastfollowup.serializer import LeadLastFollowUpSerializer

# Create your views here.
class LeadAddView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        leadserializer = LeadSerializer(data=request.data)
        if leadserializer.is_valid(raise_exception=True):
            leadserializer.save()
            # LeadFollowUp Serializer
            serviceIntrested = request.data.get("LeadServiceInterested")

            try:
                for i in serviceIntrested:
                    myData = {
                        'LeadID': leadserializer.data.get('id'),
                            'Company': request.data.get("Company"),
                            'Brand': request.data.get("Brand"),
                            'LeadRep': request.data.get("LeadRepresentativePrimary"),
                            'LeadStatus': request.data.get("LeadStatus"),
                            'LeadStatusDate': request.data.get("LeadDateTime"),
                            'LeadServiceInterested': i    
                    }
                    leadLastFollowUpserializer = LeadLastFollowUpSerializer(data=myData)
                    leadFollowupserializer = LeadFollowupSerializer(data=myData)

                    if leadFollowupserializer.is_valid() and leadLastFollowUpserializer.is_valid():
                        leadFollowupserializer.save()
                        leadLastFollowUpserializer.save()
                    else:
                        combine_error = {
                        "leadFollowUpError":leadFollowupserializer.errors,
                            "LeadLastFollowUpError": leadLastFollowUpserializer.errors ,
                        }
                        return Response(combine_error, status=status.HTTP_400_BAD_REQUEST)
                return Response(leadFollowupserializer.data, status=status.HTTP_201_CREATED)
                
            except Exception as e:
                print("ïnternal server error!!")
                return Response({"Msg":"Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        else:
            # Handle validation errors if the serializer is not valid
            return Response({"error": "Validation failed", "details": leadserializer.errors})
    def get(self, request, id = None):
        if id is not None:
            try:
                lead = Lead.objects.get(Q(id=id) & Q(LeadRepresentativeSecondary=request.user))
                print(lead)
                serializer = LeadGetSerializer(lead)

                return Response(serializer.data)
            except ObjectDoesNotExist:  # Catch ObjectDoesNotExist exception
                return Response({"Msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)      
        else:    
            if request.user.is_admin:
                lead = Lead.objects.all()
            else:
                lead = Lead.objects.filter(LeadRepresentativePrimary=request.user)  

            serializer = LeadGetSerializer(lead, many=True)
            return Response(serializer.data)
    def put(self, request, id=None):
        if id is None:
            return Response({"Msg": "Id is None"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            lead_instance = Lead.objects.get(id=id)
        except Lead.DoesNotExist:
            return Response({"Msg": "Lead not found"}, status=status.HTTP_404_NOT_FOUND)
        print("This put request is running")
        serializer = LeadSerializer(lead_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Msg":" Updated Sucessfully!!"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LeadFilterView(generics.ListCreateAPIView):  
    permission_classes = [IsAuthenticated]
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = {
    # 'LeadName': ['icontains','exact'],
    'LeadPhone': ['exact', 'icontains'],
    'LeadEmail': ['exact', 'icontains'],
    'id': ['exact'],
    'Brand': ['exact'],
    }
    def get_queryset(self):
        name = self.request.query_params.get('LeadName')
        phone = self.request.query_params.get('LeadPhone')
        email = self.request.query_params.get('LeadEmail')
        queryset = Lead.objects.all()

        if name and email and phone:
            # Use Q objects to filter for partial matches in LeadName
            queryset = queryset.filter(
                Q(LeadName__icontains=name) &
                Q(LeadPhone__icontains=phone) &
                Q(LeadEmail__icontains=email)
                )
        elif name and email:
            queryset = queryset.filter(
                Q(LeadName__icontains=name) &
                Q(LeadEmail__icontains=email) 
                
                )
        elif email and phone:
            queryset = queryset.filter(
                Q(LeadName__icontains=name)&
                Q(LeadPhone__icontains=phone)
                )
        elif name and phone:
            queryset = queryset.filter(
                Q(LeadName__icontains=name)&
                Q(LeadPhone__icontains=phone)
                )
            
        elif name:
            queryset = queryset.filter(Q(LeadName__icontains=name))
        
        elif email:
            queryset = queryset.filter(Q(LeadName__icontains=email))
        
        elif phone:
            queryset = queryset.filter(Q(LeadName__icontains=phone))


        return queryset




class LeadDetailView(RetrieveAPIView):
    renderer_classes = [UserRenderer]     
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()


