from rest_framework import serializers
from .models import LeadLastFollowUp
from service.serializers import ServiceSerializer
from myuser.serializers import UserNameSerializer
from lead.serializer import LeadGetSerializer

class LeadLastFollowUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadLastFollowUp
        fields = '__all__'
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
        elif lead_status is not None and lead_status not in [ "Distance Issue","Pricing Issue",  "Already Taken Service", "Quality Issue", "Not Interested Anymore", "Did Not Enquire", "Only Wanted Information", "Other", "Try Next Time"] and lead_status_date is None:
            raise serializers.ValidationError("Lead status date is required.")
        elif lead_event is not None and lead_event_date is None:
            raise serializers.ValidationError("Lead Event date Cannot be None")
        elif lead_event is not None and lead_event_taken_by is None:
            raise serializers.ValidationError('Please Select Who take Event')
        # Perform other validations or processing here if needed
        # ...
        return data


class LeadLastFollowupGetSerializer(serializers.ModelSerializer):
    LeadServiceInterested = ServiceSerializer()
    LeadRep = UserNameSerializer()
    LeadID = LeadGetSerializer()
    class Meta:
        model = LeadLastFollowUp
        fields = [
            "LeadFollowupID",
            "LeadID",
            "Company",
            "Brand",
            "LeadFollowupCreatedDate",
            "LeadPhonePicked",
            "LeadStatus",
            "LeadStatusDate",
            "LeadEvent",
            "LeadEventDate",
            "LeadRep",
            "LeadEventTakenBy",
            "LeadFeeOffered",
            "LeadReasonPhoneNotPicked",
            "LeadServiceInterested"
        ]