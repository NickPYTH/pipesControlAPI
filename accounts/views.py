import json

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from rest_framework.response import Response

from .models import *
from .serializers import userProfileSerializer
from django.contrib.auth.hashers import check_password, make_password


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
    post:
        Получение профиля пользователя
    """
    serializer_class = userProfileSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            user = User.objects.get(username=request.POST['username'])
            if not check_password(request.POST['password'], user.password):
                return Response('errorP')
            trips = userProfile.objects.get(user=user).trip.all()
            trip_list = []
            for trip in trips:
                trip_list.append(trip)
            return Response({
                'trips': trip_list
            })
        except:
            return Response('errorL')


class LoadTrip(APIView):
    """
    post:
        Изменение профиля пользователя
    """
    serializer_class = userProfileSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data['username']
        description = request.data['description']
        print(request.data)
        return Response('ok')
