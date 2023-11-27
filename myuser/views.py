from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from myuser.renders import UserRenderer
from myuser.serializers import MyUserRegisterSerializer, MyUserSerializers, MyUserLoginSerializer, UserProfileSerializer,UserNameSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from myuser.models import MyUser


# Create your views here.
def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Create Your Registration User Code Start Here
class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        # Retrieve all users from the database
        my_all_user = MyUser.objects.all()
        serializer = MyUserRegisterSerializer(my_all_user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = MyUserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.save()
            return Response({"msg": "Registration Sucessfully"})
        return Response({"error": "Invalid Data" }, status=status.HTTP_400_BAD_REQUEST)


class UserRegisterViewByID(APIView):
    def get(self, request, id = None):
        if id is not None:
            data = MyUser.objects.get(id=id)
            serializers = MyUserRegisterSerializer(data)
            return Response(serializers.data, status=status.HTTP_200_OK)        
        return Response({"error" : "Error Please Provide ID"})


    def put(self, request, id=None):
        try:
            myuser = MyUser.objects.get(id=id)
        except MyUser.DoesNotExist:
            return Response({"error": "Converted Student Id not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = MyUserRegisterSerializer(myuser, data=request.data ,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
class MyLogin(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format = None):
        serializers = MyUserLoginSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            email = serializers.data.get("email")
            password = serializers.data.get("password")
            user = authenticate(email = email, password = password)
            if user is not None:
                token = get_token_for_user(user)
                return Response({'token': token, 'msg': "User Login Sucessfully"})
            else:
                Response({ "error": "Invalid Data" }, status=status.HTTP_401_UNAUTHORIZED)

            if user == None:
                return Response({"error": "Invalid Data"}, status = status.HTTP_400_BAD_REQUEST)
        else:
            Response({"error": "Invalid Data"}, status=status.HTTP_400_BAD_REQUEST)


class MyProfile(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)  

class GetAllUser(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        
        if request.user.is_admin:
            user = MyUser.objects.all()
            serializer = UserNameSerializer(user, many=True) 
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Not Authenticated"}, status=status.HTTP_401_UNAUTHORIZED)



    
class GetNameById(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request, id=None):
        if id is None:
            return Response({"error": "Method Not Allowed"}, status=status.HTTP_400_BAD_REQUEST)
        userData =MyUser.objects.get(id=id) 
        serializer = MyUserRegisterSerializer(userData)
        return Response(serializer.data)

        
    

