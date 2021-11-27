from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password, make_password

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

    def post(self, request):
        username = request.POST['login']
        password = request.POST['password']
        try:
            usr_obj = User.objects.get(username=username)
            if check_password(password, usr_obj.password):
                return HttpResponse({'status': 'ok'})
            else:
                return HttpResponse({'status': 'b'})
        except:
            return HttpResponse({'status': 'e'})


class UpdateProfile(UpdateAPIView):
    """
        patch:
            Изменение данных профиля пользователя
        """
    serializer_class = userProfileSerializer
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        pass
