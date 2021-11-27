from django.urls import include, path
from .views import CreateProfile, GetProfile, LoadTrip

urlpatterns = [
    path("create-profile", CreateProfile.as_view(), name="create-profile"),
    path("get-profile", GetProfile.as_view(), name="get-profile"),
    path("load-trip", LoadTrip.as_view(), name="load-trip"),
]
