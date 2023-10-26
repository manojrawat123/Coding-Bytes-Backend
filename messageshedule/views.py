from django.shortcuts import render
from messageshedule.models import MessageSchedule
from messagetemplate.models import SMSTemplate
from messageshedule.serializers import MessageSerializer, MessageSheduleSerializers
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import datetime
from django.conf import settings
from django.core.mail import send_mail ,EmailMessage



class EmailSheduleViews(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            data = MessageSchedule.objects.get(ScheduleID= pk)
            serializer = MessageSheduleSerializers(data)
            return Response(serializer.data)
        else:
            data = MessageSchedule.objects.all()
            serializer = MessageSheduleSerializers(data, many=True)
            return Response(serializer.data)
    
    def post(self, request, pk=None):
        if pk is not None:
            return Response({"Err": "Post Method Not allowed"})
        serializer = MessageSheduleSerializers(data=request.data)
        if serializer.is_valid():
            # Save data to the database
            data = serializer.save()
            # Return a success response
            return Response({"Msg ":"Registration successfully!!"})
        return Response(serializer.errors, status=400)
    
    def put(self, request, pk):
        try:
            email_schedule = MessageSchedule.objects.get(pk=pk)
        except MessageSchedule.DoesNotExist:
            return Response({"error": "MessageSchedule not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = MessageSheduleSerializers(email_schedule, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Msg": "MessageSchedule updated successfully!!"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            email_schedule = MessageSchedule.objects.get(pk=pk)
        except MessageSchedule.DoesNotExist:
            return Response({"error": "MessageSchedule not found"}, status=status.HTTP_404_NOT_FOUND)
        email_schedule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    
class MessageSheduleOnlyEmail(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk=None):
        serializers = MessageSerializer(data=request.data)
        if serializers.is_valid():
            try:
                email_lis = serializers.data.get("emails")
                my_body = serializers.data.get("body")
                email_from = settings.EMAIL_HOST_USER
                email = "positive.mind.123456789@gmail.com"
                recipient_list = email_lis
                # subject = my_subject
                # message = f'''{my_body}'''
                # email = EmailMessage(subject, message, email_from,recipient_list)
                # email.send()
                return Response({"Msg": "Email Send Successfully!!"})
            except Exception as e:
                print(f"Email sending failed: {e}")
                return Response({"msg": "Email Failed"})
        return Response(serializers.errors, status=400)
       