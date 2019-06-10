from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict

from .models import Climbs

def index(request):
    return render(request, 'V0toV17/index.html')

def makeClimb(x):
    climb = model_to_dict(x)
    session = model_to_dict(x.session)
    climb['session'] = session
    return climb

def entries(request, user_id):
    # sessions = list(map(lambda x: x.session, serializers.serialize("json", Climbs.objects.all().prefetch_related('session'))))
    # sessions = list(map(makeClimb, Climbs.objects.all().prefetch_related('session')))
    sessions = serializers.serialize('json', Climbs.objects.all(), use_natural_foreign_keys=True, use_natural_primary_keys=True)
    return JsonResponse(sessions, safe=False)

def results(request, user_id):
    return HttpResponse("Results will go here for user {}".format(user_id))

def detail(request, user_id):
    return HttpResponse("Climbing entries for user {} to go here".format(user_id))

