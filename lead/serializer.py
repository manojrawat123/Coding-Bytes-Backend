from rest_framework import serializers
from .models import Lead
from service.serializers import ServiceSerializer
from myuser.serializers import UserNameSerializer
from leadScource.serializers import LeadScourceSerializers
from brand.serializers import BrandSerializers
from company.serializers import CompanySerializer


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'


class LeadGetSerializer(serializers.ModelSerializer):
    LeadServiceInterested = ServiceSerializer(many=True)  
    LeadRepresentativePrimary = UserNameSerializer()
    LeadRepresentativeSecondary = UserNameSerializer()
    LeadScourceId = LeadScourceSerializers()
    Brand = BrandSerializers()
    Company = CompanySerializer()
    class Meta:
        model = Lead
        fields = ["id","LeadName","LeadPhone" ,"LeadEmail", "LeadLocation","LeadAddress", "LeadScourceId" ,"LeadSource", "Company" ,"Profession",
                    "LeadStatus" ,"Brand", "PageSource" ,"Plateform", "LeadDateTime", "LeadRepresentativeSecondary", "DND" ,"LeadRepresentativePrimary", "LeadCountry", "LeadState", "LeadAssignmentAlgo",
                    "LeadNextCallDate","LeadServiceInterested"
                    ]