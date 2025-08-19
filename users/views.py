from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from .serializers import LoginSerializers, RegisterSerializers, ProfileSerializer
from chat import settings
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializers
    permission_classes = [AllowAny,]

class LoginView(APIView):
    permission_classes = [AllowAny,]

    def post(self, request):
        serializer = LoginSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        if user is not None:
            login(request, user)
            return Response({'message': 'Login Successful'}, status=status.HTTP_200_OK)
        return Response({'message': 'Login Failed'}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logout Successful'}, status=status.HTTP_200_OK)

class  ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user
