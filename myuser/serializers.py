from rest_framework import serializers
from myuser.models import MyUser
from brand.models import Brand

class MyUserSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type":"password"}, write_only = True)
    class Meta:
        model = MyUser
        fields = ["email","name", "phone","company", "brand", "password", "password2"]
        extra_kwargs = {
            'password':{'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        if password != password2:
            raise serializers.ValidationError("Password Didn't match")
        return attrs
    
    def create(self, validate_data):
        validate_data.pop('password2')
        return MyUser.objects.create_user(**validate_data)
    

class MyUserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = "__all__" 

class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ["id", "name"]
    

    
class MyUserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 225)
    class Meta:
        model = MyUser
        fields = ["email", "password"]

    def validate(self, data):
        for field_name, value in data.items():
            if value == "":
                raise serializers.ValidationError(f"{field_name} field is required.")
        return data




class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand

        fields = ('id', 'BrandName')


class UserProfileSerializer(serializers.ModelSerializer):
  brand = BrandSerializer(many=True)  #
  class Meta:
    model = MyUser
    fields = ["id","email","name", "phone","company", "brand"]
    def to_representation(self, instance):
        """
        Serialize the instance to a representation.
        """
        ret = super().to_representation(instance)

        # Get the brand IDs associated with the user
        brand_ids = ret['brand']

        # Fetch the brand details from the database
        brands = Brand.objects.filter(id__in=brand_ids).values('id', 'name')

        # Replace the brand field in the response with the full brand details
        ret['brand'] = list(brands)

        return ret
    