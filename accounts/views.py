from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from rest_framework.response import Response

from .models import userProfile
from .serializers import userProfileSerializer


class CreateProfile(CreateAPIView):
    """
    post:
      Создание профиля пользователя
    """
    serializer_class = userProfileSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        return self.serializer_class


class GetProfile(APIView):
    """
    get:
        Получение профиля пользователя
    """
    serializer_class = userProfileSerializer
    permission_classes = [AllowAny]

    def get(self, request):
        username = self.request.user
        user = User.objects.get(username=username)
        user_profile = userProfile.objects.filter(user=user)
        user_info = {
            'username': user.username,
            'email': user.email,
        }
        return Response(user_info)
