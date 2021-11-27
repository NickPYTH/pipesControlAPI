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

    def get(self, request):
        username = self.request.user
        user = User.objects.get(username=username)
        print(user)
        user_profile = userProfile.objects.filter(user=user)
        print(user_profile)
        user_info = {
            'username': user.username,
            'email': user.email,
            'forms': ['formName']
        }
        return Response(user_info)

    def post(self, request):
        username = request.POST['login']
        password = request.POST['password']
        try:
            usr_obj = User.objects.get(username=username)
            if check_password(password, usr_obj.password):
                return {'status': 'ok'}
            else:
                return {'status': 'b'}
        except:
            return {'status': 'e'}


class UpdateProfile(UpdateAPIView):
    """
        patch:
            Изменение данных профиля пользователя
        """
    serializer_class = userProfileSerializer
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        pass
