from rest_framework import serializers
from leadfollowup.models import LeadFollowUp

class LeadFollowupSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadFollowUp
        fields = '__all__'
        extra_kwargs = {
            'LeadEventTakenBy': {'required': False}  # This makes the field not required
        }
    def validate(self, data):
        lead_phone_picked = data.get('LeadPhonePicked')
        lead_event = data.get('LeadEvent')
        lead_status = data.get('LeadStatus')
        lead_status_date = data.get('LeadStatusDate')
        lead_event_date = data.get('LeadEventDate')
        lead_event_taken_by = data.get('LeadEventTakenBy')
        
        if lead_phone_picked is None and lead_event is None and lead_status != "Fresh":
            raise serializers.ValidationError("Please select one option to proceed.")
        elif lead_phone_picked is not None and lead_event is not None:
            raise serializers.ValidationError("Only one of LeadPhonePicked or LeadEvent should be provided.")
        elif lead_phone_picked == "Yes" and lead_status is None:
            raise serializers.ValidationError("Please Select Lead Status")
        elif lead_status is not None and lead_status not in [ "Distance Issue","Pricing Issue",  "Already Taken Service", "Quality Issue", "Not Interested Anymore", "Did Not Enquire", "Only Wanted Information", "Other"] and lead_status_date is None:
            raise serializers.ValidationError("Lead status date is required.")
        elif lead_event is not None and lead_event_date is None:
            raise serializers.ValidationError("Lead Event date Cannot be None")
        elif lead_event is not None and lead_event_taken_by is None:
            raise serializers.ValidationError('Please Select Who take Event')
        # Perform other validations or processing here if needed
        # ...
        return data
