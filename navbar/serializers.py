from rest_framework import serializers
from navbar.models import MenuItem

class NavBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'