from django.http import JsonResponse
from .models import *

def getLligues(request):
    jsonData = list( Lliga.objects.all().values() )
    return JsonResponse({
            "status": "OK",
            "lligues": jsonData,
        }, safe=False)

def getEquips(request, lliga_id):
    lliga = Lliga.objects.get(pk=lliga_id)
    equips = lliga.equips
    jsonData = list ( equips.values())
    return JsonResponse({
            "status": "OK",
            "equips": jsonData,
        }, safe=False)

