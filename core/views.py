import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, ListView
from django.utils import timezone
from core import models


class Index(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c['person_name'] = 'Masha'
        return c

class Person(ListView):
    model = models.Person




# def index(request):
#     #now = timezone.now()
#     # return HttpResponse(f'<h1>Текущее время</h1>{now}')
#     person = models.Person.objects.first()
#     response = render(request, "core/index.html", context={'person': person})
#     return response

def persons(request):
    object_list = []
    for p in models.Person.objects.all():
        object_list.append({
            'id': p.id,
            'name': p.name,
        })
    return JsonResponse({'objects' : object_list})

# def person(request, id):
#     p = models.Person.objects.get(id=id)
#     detal = {
#         'id': p.id,
#         'name': p.name,
#         'phone': p.phone
#     }
#     return JsonResponse(detal)
