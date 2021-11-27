from django.urls import include, path
from .views import CreateProfile, GetProfile

urlpatterns = [
    path("create-profile", CreateProfile.as_view(), name="create-profile"),
    path("get-profile", GetProfile.as_view(), name="get-profile"),
]
