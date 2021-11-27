from django.db import models
from django.contrib.auth.models import User


class MarkerCoordinate(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300, null=True, blank=True)
    latitude = models.CharField(max_length=300)
    longitude = models.CharField(max_length=300)
    dateTime = models.DateTimeField()


class TripCoordinates(models.Model):
    latitude = models.CharField(max_length=300)
    longitude = models.CharField(max_length=300)


class Trip(models.Model):
    startDateTime = models.DateTimeField()
    endDateTime = models.DateTimeField()
    coordinates = models.ManyToManyField(TripCoordinates)


class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    trip = models.ManyToManyField(Trip)



