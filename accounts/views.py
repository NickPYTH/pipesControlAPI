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


class GetTripDetail(APIView):
    """
    post:
        Получение профиля пользователя
    """
    serializer_class = userProfileSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            user = User.objects.get(username=request.POST['username'])
            description = request.POST['description']
            trip = userProfile.objects.get(user=user).trip.filter(description=description)[0]
            markers = []
            way = []
            for marker in trip.markers.all():
                markers.append(
                    {
                        'name': marker.name,
                        'description': marker.description,
                        'latitude': marker.latitude,
                        'longitude': marker.longitude,
                    }
                )
            for step in trip.coordinates.all():
                way.append({
                    "latitude": step.latitude,
                    "longitude": step.longitude
                })
            return Response({
                'markers': markers,
                'way': way
            })
        except:
            return Response('errorL')


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
                trip_list.append({
                    'description': trip.description,
                    'date_time': trip.dateTime,
                    'num_markers': len(trip.markers.all())
                })
            print(trip_list)
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
        markers = request.data.get('markers')
        way = request.data.get('way')
        user_obj = userProfile.objects.get(user=User.objects.get(username=username))
        trip_obj = Trip.objects.create(description=description)

        for marker in markers:
            marker_obj = MarkerCoordinate.objects.create(
                name=marker.get('name'),
                description=marker.get('description'),
                latitude=marker.get('latitude'),
                longitude=marker.get('longitude')
            )
            trip_obj.markers.add(marker_obj)

        for step in way:
            coordinates_obj = TripCoordinates.objects.create(
                latitude=step.get('latitude'),
                longitude=step.get('longitude')
            )
            trip_obj.coordinates.add(coordinates_obj)

        trip_obj.save()
        user_obj.trip.add(trip_obj)
        user_obj.save()

        return Response('ok')
