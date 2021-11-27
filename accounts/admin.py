from django.contrib import admin
from .models import *

admin.site.register(userProfile)
admin.site.register(MarkerCoordinate)
admin.site.register(TripCoordinates)
admin.site.register(Trip)

admin.site.site_header = "voteAppAdmin"
