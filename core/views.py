import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from core import models


def index(request):
    #now = timezone.now()
    # return HttpResponse(f'<h1>Текущее время</h1>{now}')
    person = models.Person.objects.first()
    response = render(request, "core/index.html", context={'person': person})
    return response

def persons(request):
    object_list = []
    for p in models.Person.objects.all():
        object_list.append({
            'id': p.id,
            'name': p.name,
        })
    return JsonResponse({'objects' : object_list})
