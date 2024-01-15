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
from myuser.models import MyUser
from django.db.models import Min
from usercourse.models import UserCourse
from messageshedule.views import send_sms
from brand.models import Brand
from service.models import Service
from emailshedule.views import custom_email_func
from datetime import date, datetime
from leadScource.models import LeadSource
from leadScource.serializers import LeadScourceSerializers
from service.serializers import ServiceSerializer
from lead.googletoken import verify_not_robot_func
from datetime import datetime, timedelta
from django.utils import timezone

# Create your views here.
class LeadAddView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        leadserializer = LeadSerializer(data=request.data)
        userID = request.data.get("LeadRepresentativePrimary")
        brandId = request.data.get("Brand")
        courseId = request.data.get("LeadServiceInterested")
        companyID = request.data.get("Company")
        # Code Of FaceBook Leads
        if userID is None:
            token = request.data.get("captcha_token") 
            try:

                response = verify_not_robot_func(token)
                print(response)
            except Exception as e:
                return Response({"error": "You Are not a Robot"}, status=status.HTTP_400_BAD_REQUEST)
            # Only Save the Code When Valid Token
            if response == "humman":
                courseAssign = list(UserCourse.objects.filter(Q(CourseID = courseId[0]) & Q(BrandID = brandId) & Q(CompanyID=companyID )).values_list("UserID", flat=True))
                myuser = list(MyUser.objects.filter(Q(brand = brandId) & Q (is_active = True)).values_list("id", flat=True))
                courseAssignActive = [x for x in myuser if x in courseAssign]
                if (len(courseAssignActive) == 0):
                    print("No Active User Allocated For this Brand")
                    return Response({"Error": "No Brand Allocated"}, status= status.HTTP_400_BAD_REQUEST)
                elif (len(courseAssignActive) == 1):
                    request.data["LeadRepresentativePrimary"] = courseAssignActive[0]
                    request.data["LeadRepresentativeSecondary"] = courseAssignActive[0]
                    userID = courseAssignActive[0]
                # Thirld Filter List of smallest Lead Add
                elif(len(courseAssignActive ) > 1):
                    smallest_weightage = UserCourse.objects.aggregate(Min('CourseWeightage'))['CourseWeightage__min']
                    user_courses_with_smallest_weightage = list(UserCourse.objects.filter(CourseWeightage=smallest_weightage).values_list("UserID", flat=True))
                    courseAssignActiveSmallest = [x for x in courseAssignActive if x in user_courses_with_smallest_weightage]

                    # Fourth Filter Last Lead
                    if (len(courseAssignActiveSmallest) == 1):
                        request.data["LeadRepresentativePrimary"] = courseAssignActiveSmallest[0]
                        
                        request.data["LeadRepresentativeSecondary"] = courseAssignActive[0]
                        userID = courseAssignActiveSmallest[0]

                    elif (len(courseAssignActiveSmallest ) > 1):
                        last_lead_user = Lead.objects.all().latest("id").LeadRepresentativePrimary.id
                        courseAssignActSmNotLastLead = [x for x in courseAssignActiveSmallest if x  != last_lead_user]
                        userID = courseAssignActSmNotLastLead[0]
                        request.data["LeadRepresentativePrimary"] =courseAssignActSmNotLastLead[0]
                        request.data["LeadRepresentativeSecondary"] = courseAssignActive[0]
                        
                userPriority = UserCourse.objects.get(Q(UserID = userID)& Q(CourseID =courseId[0]))
                userPriority.CourseWeightage = userPriority.CourseWeightage + 1
                userPriority.save()
                # return Response({"message": "Lead saved successfully"})
            else:
                # Return an error response if the reCAPTCHA assessment is invalid
                return Response({"error": "You are not humman"}, status=400)
                

            


        if leadserializer.is_valid(raise_exception=True):
            leadserializer.save()
            serviceIntrested = request.data.get("LeadServiceInterested")
            try:
                for i in serviceIntrested:
                    myData = {
                        'LeadID': leadserializer.data.get('id'),
                            'Company': request.data.get("Company"),
                            'Brand': request.data.get("Brand"),
                            'LeadRep': userID,
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
                for i in courseId:
                    # send_sms(1, leadID = leadserializer.data.get("id"), name= request.data.get("LeadName"), phone=request.data.get("LeadPhone"), brandId=brandId, serviceId=i, companyId=companyID,leadRepId=userID) 
                    try:
                        leadID = leadserializer.data.get("id")
                        leadObj = Lead.objects.get(id = leadID)
                        custom_email_func(4, newLead=True,leadObj=leadObj, serviceID = i,)
                    except Exception as e:
                        print("Email Fail")
                
                return Response(leadFollowupserializer.data, status=status.HTTP_201_CREATED)  
            except Exception as e:
                print("Internal Server Error")
                return Response({"Msg":"Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"error": "Validation failed", "details": leadserializer.errors})
        
   
    def get(self, request, id = None):
        if id is not None:
            try:
                lead = Lead.objects.get(Q(id=id) & Q(LeadRepresentativeSecondary=request.user))
                serializer = LeadGetSerializer(lead)

                return Response(serializer.data)
            except ObjectDoesNotExist:  # Catch ObjectDoesNotExist exception
                return Response({"Msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)      
        else:   
            now = timezone.now().date()
            last_month = now - timedelta(days=30)
            
            to_date_pr = request.query_params.get('to_date', now)
            from_date_pr = request.query_params.get('from_date', last_month) 
            all_leads_params = request.query_params.get('all', None)  
            from_date = datetime.strptime(f"{to_date_pr}", "%Y-%m-%d").strftime("%Y-%m-%dT23:59:00Z")
            to_date = datetime.strptime(f"{from_date_pr}", "%Y-%m-%d").strftime("%Y-%m-%dT00:00:00Z")  
            
            # Geting All Leads
            if all_leads_params == "all":
                if request.user.is_admin:
                    lead = Lead.objects.all()  
                else:
                    lead = Lead.objects.filter(LeadRepresentativePrimary=request.user)  
                serializer = LeadGetSerializer(lead, many=True)
                return Response(serializer.data)
            
            else:
                if request.user.is_admin:
                    lead = Lead.objects.filter(Q(LeadDateTime__lt = from_date) & Q(LeadDateTime__gt = to_date)) 
                else:
                    lead = Lead.objects.filter(Q(LeadRepresentativePrimary=request.user) & Q(LeadDateTime__lt = from_date) & Q(LeadDateTime__gt = to_date))  
                serializer = LeadGetSerializer(lead, many=True)
                return Response(serializer.data)
            

    def put(self, request, id=None):
        if id is None:
            return Response({"Msg": "Id is None"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            lead_instance = Lead.objects.get(id=id)
        except Lead.DoesNotExist:
            return Response({"Msg": "Lead not found"}, status=status.HTTP_404_NOT_FOUND)
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


class AddCourseLeadView(APIView):
    def put(self, request,id=None):
        # Method Not Allowed
        if id is None or request.data.get("LeadServiceInterested") is None:
            return Response({"Msg": "Id is None"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            lead_instance = Lead.objects.get(id=id)
            service_interested_data = request.data.get('LeadServiceInterested', [])
            existing_service_interested = list(lead_instance.LeadServiceInterested.values_list('id', flat=True))
            updated_service_interested = list(set(existing_service_interested) | set(service_interested_data))
            lead_instance.LeadServiceInterested.set(updated_service_interested)
            request.data['LeadServiceInterested'] = updated_service_interested
            print(lead_instance.LeadServiceInterested)
            for i in service_interested_data:
                try:
                    lead_follow_up = {
                        "LeadID" : id,
                        "Company": lead_instance.Company.id,
                        "Brand": lead_instance.Brand.id,
                        "LeadStatus": "Fresh",
                        "LeadRep": lead_instance.LeadRepresentativePrimary.id, 
                        "LeadServiceInterested": i ,
                        "LeadStatusDate":  datetime.combine(date.today(), datetime.min.time())
                    }
                    leadFollowUpSerializer = LeadFollowupSerializer(data=lead_follow_up)
                    lead_last_follow_serializer = LeadLastFollowUpSerializer(data=lead_follow_up)
                    if leadFollowUpSerializer.is_valid():
                        leadFollowUpSerializer.save()
                    else:
                        return Response(leadFollowUpSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    
                    if lead_last_follow_serializer.is_valid():
                        lead_last_follow_serializer.save()
                    else:
                        return Response(lead_last_follow_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                except Exception as e:
                    print("Some Error Occured")
                    print(e)
                    return Response({"error": "Some Error Occured In Backend"}, status=status.HTTP_400_BAD_REQUEST)
        except Lead.DoesNotExist:
            return Response({"Msg": "Lead not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = LeadSerializer(lead_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response({"Msg":" Updated Sucessfully!!"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LeadDetailView(RetrieveAPIView):
    renderer_classes = [UserRenderer]     
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()

# DashBoard Page Api
class AddNewLeadGetApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id = None):
        if id == None:
            return Response({"error": "Method Not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else: 

            # Lead Scource
            leadScource = LeadSource.objects.filter(Brand = id)
            lead_scource_serializer = LeadScourceSerializers(leadScource,many=True)

            # Get Services 
            services = Service.objects.filter(Brand_id=id)
            serializer = ServiceSerializer(services, many=True)
            return Response({"lead_scource": lead_scource_serializer.data, "service": serializer.data}, status=status.HTTP_200_OK)