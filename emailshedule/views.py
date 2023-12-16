from django.shortcuts import render
from emailshedule.models import EmailSchedule
from emailshedule.serializers import EmailSheduleSerializers, EmailSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail ,EmailMessage
from emailtemplate.models import EmailTemplate
from myuser.models import MyUser
from service.models import Service
from leadScource.models import LeadSource
from lead.models import Lead
from feetracer.models import Fee
from payment.models import Payment
from paymentmode.models import PaymentMode
from paymenttype.models import PaymentType
from brand.models import Brand
from convertedstudent.models import convertedstudent


class EmailSheduleViews(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            data = EmailSchedule.objects.get(ScheduleID= pk)
            serializer = EmailSheduleSerializers(data)
            return Response(serializer.data)
        else:
            data = EmailSchedule.objects.all()
            serializer = EmailSheduleSerializers(data, many=True)
            return Response(serializer.data)
    
    def post(self, request, pk=None):
        if pk is not None:
            return Response({"Err": "Post Method Not allowed"})
        serializer = EmailSheduleSerializers(data=request.data)
        if serializer.is_valid():
            # Save data to the database
            data = serializer.save()
            # Return a success response
            return Response({"Msg ":"Registration successfully!!"})
        return Response(serializer.errors, status=400)
    
    def put(self, request, pk):
        try:
            email_schedule = EmailSchedule.objects.get(pk=pk)
        except EmailSchedule.DoesNotExist:
            return Response({"error": "EmailSchedule not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmailSheduleSerializers(email_schedule, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Msg": "EmailSchedule updated successfully!!"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            email_schedule = EmailSchedule.objects.get(pk=pk)
        except EmailSchedule.DoesNotExist:
            return Response({"error": "EmailSchedule not found"}, status=status.HTTP_404_NOT_FOUND)
        email_schedule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    
class EmailSheduleOnlyEmail(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk=None):
        serializers = EmailSerializer(data=request.data)
        if serializers.is_valid():
            try:
                email_lis = serializers.data.get("emails")
                message_id = serializers.data.get("template_id")
                email_template = EmailTemplate.objects.get(TemplateID = message_id)
                my_subject = serializers.data.get("subject")
                my_body = serializers.data.get("body")
                email_from = settings.EMAIL_HOST_USER
                email = "positive.mind.123456789@gmail.com"
                recipient_list = email_lis
                subject = my_subject
                message = f'''{my_body}'''
                email = EmailMessage(subject, message, email_from,recipient_list)
                email.send()
                
                return Response({"Msg": "Email Send Successfully!!"})
            except Exception as e:
                print(f"Email sending failed: {e}")
                return Response({"msg": "Email Failed"})
        return Response(serializers.errors, status=400)
       

def custom_email_func(tempid = None, newLead = None,leadObj = None, addPayment = None, convertLead = None, addPendingFees = None, serviceID = None,leadID=None,userID=None, feesID=None, studendtId = None , convertedId= None, paymentId=None,):
    try:
        if newLead == True:
            # varaibles
            brand_obj = Brand.objects.get(id = leadObj.Brand.id)
            brand_name = brand_obj.BrandName
            brand_email = brand_obj.BrandEmail
            company_user = MyUser.objects.filter(company = leadObj.Company.id)
            formatted_strings = [
                f'{user.name} ({user.email})' for user in company_user
            ]

            print("Debug1")
            company_user_str = ', '.join(formatted_strings)
            

            print(company_user_str)
            coursename = Service.objects.get(id = serviceID).ServiceName
            subject = EmailTemplate.objects.get(TemplateID = tempid).TemplateMessage.format(
                
                StudentName=leadObj.LeadName,
                Course = coursename
            )

            # Lead.objects.get().
            print(leadObj.LeadRepresentativePrimary)   
            user_name = MyUser.objects.get(id = leadObj.LeadRepresentativePrimary.id).name
            # Format date and time into required formats
            date_object = datetime.strptime(f"{leadObj.LeadDateTime}", "%Y-%m-%d %H:%M:%S%z")
            lead_date = date_object.strftime("%d %b %Y")  # 1 Dec 2023
            lead_time = date_object.strftime("%H:%M")     # 11:39
            print(lead_date, lead_time)
            lead_scource = LeadSource.objects.get(LeadSourceID = leadObj.LeadScourceId.LeadSourceID).LeadSource
            body = EmailTemplate.objects.get(TemplateID= tempid).TemplateBody.format(
                today_date = f"{lead_date} {lead_time}",
                company_user_str = company_user_str,
                brand_email = brand_email,
                brand_name = brand_name,
                AssignedTo=user_name,
                StudentName=leadObj.LeadName, 
                Phone=leadObj.LeadPhone,
                Email=leadObj.LeadEmail,
                LeadID=leadObj.id, 
                BrandLeadID=leadObj.Brand, 
                LeadDate=lead_date,
                LeadTime=lead_time,
                Course = coursename,
                ClassMode=leadObj.LeadAssignmentAlgo,
                State=leadObj.LeadAddress,
                Country=leadObj.LeadLocation,
                UserLocation=leadObj.LeadLocation,
                LeadSource = lead_scource,
                UpdatedBy=user_name
            )
            recipient_list = [email for email in company_user]
            print(recipient_list)
            from_email = 'positive.mind.123456789@gmail.com'
            email = EmailMessage(subject, body, from_email, recipient_list)
            email.content_subtype = "html"
            email.send()
        if addPendingFees == True:
            leadObj = Lead.objects.get(id=leadID)
            feesObj = Fee.objects.get(id = feesID)
            user_name = MyUser.objects.get(id= leadObj.LeadRepresentativePrimary.id).name
            company_user = MyUser.objects.filter(company = leadObj.Company.id)
            formatted_strings = [
                f'{user.name} ({user.email})' for user in company_user
            ]
            brand_name = Brand.objects.get(id = leadObj.Brand.id)
            date_object = datetime.strptime(f"{feesObj.fee_payment_datetime}", "%Y-%m-%d")
            fees_date = date_object.strftime("%d %b %Y")  # 1 Dec 2023
            fees_time = date_object.strftime("%H:%M")     # 11:39
            print("Debug1")
            company_user_str = ', '.join(formatted_strings)
            subject = EmailTemplate.objects.get(TemplateID= tempid).TemplateMessage.format(
                rep_name = user_name,
                StudentName = leadObj.LeadName
            )
            convertedObj = convertedstudent.objects.get(ConvertedID = feesObj.converted_id.ConvertedID)

            course_name = Service.objects.get(id = convertedObj.CourseID.id).ServiceName
            lead_scource = LeadSource.objects.get(LeadSourceID = leadObj.LeadScourceId.LeadSourceID).LeadSource
            payments = Payment.objects.filter(lead_id=leadObj.id)
            total_fees = sum(i.payment_amount for i in payments)
            existing_payment_ids = Fee.objects.filter(payment_id__isnull=False).values_list('payment_id', flat=True)
            payments_done_obj = Payment.objects.filter(lead_id=leadObj.id, payment_id__in=existing_payment_ids)
            payment_done = sum(i.payment_amount for i in payments_done_obj)
            pending_fees = total_fees - payment_done
            body = EmailTemplate.objects.get(TemplateID= tempid).TemplateBody.format(
            fees_paid = payment_done,
            total_fees = total_fees,
            outstanding_fees = pending_fees,
            next_due_date = feesObj.next_due_date,
            rep_name = user_name,
            fees_id = feesID,
            payment_id = feesObj.payment_id,
            converted_id = feesObj.converted_id,
            payment_date = feesObj.fee_payment_datetime,
            payment_time = feesObj.fee_payment_datetime,
            customer_name = leadObj.LeadName,
            customer_email = leadObj.LeadEmail,
            lead_id = feesObj.lead,
            lead_scource = lead_scource,
            lead_date = leadObj.LeadDateTime,
            lead_time="",
            today_date = f"{fees_date} {fees_time}",
            brand_name = brand_name,
            LeadName = leadObj.LeadName,
            CourseName = course_name,
            company_user_str = company_user_str
            )
            from_email = 'positive.mind.123456789@gmail.com'
            recipient_list = [email for email in company_user]
            email = EmailMessage(subject, body, from_email, recipient_list)
            email.content_subtype = "html"
            email.send()
        if convertLead == True:
            leadObj = Lead.objects.get(id = leadID)
            representative = MyUser.objects.get(id = leadObj.LeadRepresentativePrimary.id)
            brand_obj = Brand.objects.get(id = leadObj.Brand.id)
            brand_name = brand_obj.BrandName
            brand_email = brand_obj.BrandEmail
            company_user = MyUser.objects.filter(company = leadObj.Company.id)
            formatted_strings = [
                f'{user.name} ({user.email})' for user in company_user
            ]
            company_user_str = ', '.join(formatted_strings)
            date_object = datetime.strptime(f"{leadObj.LeadDateTime}", "%Y-%m-%d %H:%M:%S%z")
            lead_date = date_object.strftime("%d %b %Y")  # 1 Dec 2023
            lead_time = date_object.strftime("%H:%M")     # 11:39
            print(lead_date, lead_time)
            convertedLeadObj = convertedstudent.objects.get(ConvertedID = convertedId)
            payment_done = Payment.objects.get(payment_id = convertedLeadObj.PaymentID.payment_id).payment_amount
            today_date_object = datetime.strptime(f"{convertedLeadObj.ConvertedDateTime}", "%Y-%m-%d %H:%M:%S.%f%z")
            convert_date = today_date_object.strftime("%d %b %Y")  # 1 Dec 2023
            convert_time = today_date_object.strftime("%H:%M")     # 11:39
            lead_scource = LeadSource.objects.get(LeadSourceID = leadObj.LeadScourceId.LeadSourceID)
            
            subject = EmailTemplate.objects.get(TemplateID= tempid).TemplateMessage.format(
                StudentName=leadObj.LeadName,
                Course = convertedLeadObj.CourseName
            )
            body = EmailTemplate.objects.get(TemplateID= tempid).TemplateBody.format(
                ConvertedID = convertedId,
                LeadID = convertedLeadObj.LeadID, #
                CourseName = convertedLeadObj.CourseName, #  
                CourseID = convertedLeadObj.CourseID, #
                TotalFee = convertedLeadObj.TotalFee,#
                StudentID = studendtId,#
                Representative = representative,
                Brand = convertedLeadObj.Brand,#
                Company = convertedLeadObj.Company,#
                PaymentID = convertedLeadObj.PaymentID, #
                LeadName = leadObj.LeadName, #
                LeadEmail = leadObj.LeadEmail, #
                LeadPhone = leadObj.LeadPhone, #
                lead_time = f"{lead_date} {lead_time}",
                brand_name = brand_name,
                brand_email = brand_email ,
                company_user_str = company_user_str,
                fees_paid = payment_done,
                today_date = f"{convert_date} {convert_time}",
                LeadScource = lead_scource
            )
            from_email = 'positive.mind.123456789@gmail.com'
            recipient_list = [email for email in company_user]
            email = EmailMessage(subject, body, from_email, recipient_list)
            email.content_subtype = "html"
            email.send()
            pass
        if addPayment == True:
            # Varaibles
            leadObj = Lead.objects.get(id = leadID)
            paymentObj = Payment.objects.get(payment_id = paymentId)
            
            course_name = Service.objects.get(id = paymentObj.payment_purpose.id).ServiceName
            subject = EmailTemplate.objects.get(TemplateID= tempid).TemplateMessage.format(
                LeadName = paymentObj.name,
                course_name = course_name
            )
            # Company Email and name
            company_user = MyUser.objects.filter(company = leadObj.Company.id)
            formatted_strings = [
                f'{user.name} ({user.email})' for user in company_user
            ]

            date_object = datetime.strptime(f"{paymentObj.payment_date}", "%Y-%m-%d %H:%M:%S%z")
            payment_date = date_object.strftime("%d %b %Y")  # 1 Dec 2023
            payment_time = date_object.strftime("%H:%M")   

            print(formatted_strings)
            company_user_str = ', '.join(formatted_strings)
            print(company_user_str)
            from_email = 'positive.mind.123456789@gmail.com'
            recipient_list = [email for email in company_user]
            user_name = MyUser.objects.get(id = paymentObj.user_id.id).name
            payment_mode = PaymentMode.objects.get(payment_mode_id = paymentObj.payment_mode_id.payment_mode_id).payment_mode_display
            brand_id = paymentObj.brand.id
            brand_name = Brand.objects.get(id = brand_id).BrandName
            body = EmailTemplate.objects.get(TemplateID = tempid).TemplateBody.format(
                course_name = course_name,# 
                StudentName = paymentObj.name,
                payment_id = paymentId,
                payment_confirmation_id = paymentObj.payment_confirmation_id,
                name = paymentObj.name,#
                brand = brand_name,
                phone = paymentObj.phone,#
                email = paymentObj.email,#
                payment_date = paymentObj.payment_date,#
                payment_amount = paymentObj.payment_amount,#
                payment_currency = paymentObj.payment_currency,#
                payment_purpose = paymentObj.payment_purpose,#
                payment_type = paymentObj.payment_type,#
                payment_mode = payment_mode,#
                user_name = user_name,#
                LeadName = paymentObj.name,#
                LeadEmail =  paymentObj.email,#
                LeadPhone =  paymentObj.phone,#
                brand_name = brand_name,
                today_date = f"{payment_date} {payment_time}",
                Course = course_name,
                company_user_str = company_user_str
            )
            email = EmailMessage(subject, body, from_email, recipient_list)
            email.content_subtype = "html"
            print("debug4")
            email.send()
        print("email send sucessfully")
    except Exception as e:
        print(e)
        print("Some Error Occured!!")