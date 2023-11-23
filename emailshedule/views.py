from django.shortcuts import render
from emailshedule.models import EmailSchedule
from emailshedule.serializers import EmailSheduleSerializers, EmailSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import datetime
from django.conf import settings
from django.core.mail import send_mail ,EmailMessage
from emailtemplate.models import EmailTemplate



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
       