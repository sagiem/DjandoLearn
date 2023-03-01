import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, ListView
from django.utils import timezone
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from  rest_framework.viewsets import ReadOnlyModelViewSet
from core import models
from core import filters
from core import serializers


class TagViewSet(ReadOnlyModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.Tag
    filterset_class = filters.Tag


# class Tags(ListAPIView):
#     queryset = models.Tag.objects.all()
#     serializer_class = serializers.Tag
#     filterset_class = filters.Tag
#
#     def list(self, request, *args, **kwargs):
#         serializer = serializers.tagSearch(data=request.query_params)
#         serializer.is_valid(raise_exception=True)
#
#         return  super().list(request, *args, **kwargs)

class Tag(RetrieveAPIView):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.Tag

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

# def persons(request):
#     object_list = []
#     for p in models.Person.objects.all():
#         object_list.append({
#             'id': p.id,
#             'name': p.name,
#         })
#     return JsonResponse({'objects' : object_list})

def person(request, id):
    p = models.Person.objects.get(id=id)
    detal = {
        'id': p.id,
        'name': p.name,
        'phone': p.phone
    }
    return JsonResponse(detal)


