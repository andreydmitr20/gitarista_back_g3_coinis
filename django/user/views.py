from django.shortcuts import render
from django.core.exceptions import ValidationError
from rest_framework import views, response, exceptions, permissions, status
from django.contrib.auth import get_user_model, authenticate , login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from .serializer import UserRegisterSerializer,UserLoginSerializer,UserSerializer
UserModel = get_user_model()
# Create your views here.

# def custom_validation(data):
#     first_name = data['first_name'].strip()
#     last_name = data['last_name'].strip()
#     email = data['email'].strip()
#     password = data['password'].strip()
#     ##
#     if not email or UserModel.objects.filter(email=email).exists():
#         raise ValidationError('choose another email')
#     ##
#     if not password or len(password) < 8:
#         raise ValidationError('choose another password, min 8 characters')
    
# def validate_email(data):
#     email = data['email'].strip()
#     if not email:
#         raise ValidationError('an email is needed')
#     return True

# def validate_password(data):
#     password = data['password'].strip()
#     if not password:
#         raise ValidationError('a password is needed')
#     return True

class UserRegister(views.APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        # fix validation part!
        # clean_data = custom_validation(request.data)
        clean_data = request.data
        serializer = UserRegisterSerializer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(clean_data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        # return (request.data)
    
class UserLogin(views.APIView):
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)

    def post(self, request):
        data = request.data
        # validate_email(data)
        # validate_password(data)
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            login(request, user)
            return Response({'msg': 'User Logged in'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class UserLogout(views.APIView):

    def post(self, request):
        logout(request)
        return Response({'msg': 'User Logged out'},status=status.HTTP_200_OK)
    
class UserView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'user':serializer.data}, status=status.HTTP_200_OK)