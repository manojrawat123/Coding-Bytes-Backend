# from rest_framework import serializers
# from .models import LeadLastFollowUp

# class LeadLastFollowUpSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LeadLastFollowUp
#         fields = '__all__'

#     def create(self, validated_data):
#         lead_id = validated_data.get('LeadID')
        
#         try:
#             # Check if a record with the given lead_id exists
#             lead_followup = LeadLastFollowUp.objects.get(LeadID=lead_id)
#             for attr, value in validated_data.items():
#                 setattr(lead_followup, attr, value)
#             lead_followup.save()
#             return lead_followup
#         except LeadLastFollowUp.DoesNotExist:
#             return LeadLastFollowUp.objects.create(**validated_data)
