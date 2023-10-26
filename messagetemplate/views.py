from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from messagetemplate.models import SMSTemplate
from messagetemplate.serializers import MessageTemplateSerializers
from rest_framework.permissions import IsAuthenticated

class MessageTemplateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):
        if pk is not None:
            data = SMSTemplate.objects.get(ScheduleID= pk)
            serializer = MessageTemplateSerializers(data)
            return Response(serializer.data)
        else:
            data = SMSTemplate.objects.all()
            serializer = MessageTemplateSerializers(data, many=True)
            return Response(serializer.data)
    
    def post(self, request, pk=None):
        if pk is not None:
            return Response({"Err": "Post Method Not allowed"})
        serializer = MessageTemplateSerializers(data=request.data)
        if serializer.is_valid():
            # Save data to the database
            data = serializer.save()
            # Return a success response
            return Response({"Msg ":"Registration successfully!!"})
        return Response(serializer.errors, status=400)
    
    def put(self, request, pk):
        try:
            message_schedule = SMSTemplate.objects.get(pk=pk)
        except SMSTemplate.DoesNotExist:
            return Response({"error": "messageSchedule not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = MessageTemplateSerializers(message_schedule, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Msg": "messageSchedule updated successfully!!"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            message_schedule = SMSTemplate.objects.get(pk=pk)
        except SMSTemplate.DoesNotExist:
            return Response({"error": "messageSchedule not found"}, status=status.HTTP_404_NOT_FOUND)

        message_schedule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    


