from ninja import NinjaAPI
from .models import *

api = NinjaAPI()

@api.post("login")
def get_stats_data(request):
    return {'status': 'ok'}
