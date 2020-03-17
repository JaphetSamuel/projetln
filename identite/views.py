from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.core.serializers import serialize

# Create your views here.


def listEleve (request):
    data = serialize('json', Eleve.objects.all())
    return JsonResponse(data, safe=False)


def listProffesseur(req):
    data = serialize('json', Professeur.objects.all())
    return JsonResponse(data,safe=False)
