from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

def index(request):
    now = timezone.now()
    # return HttpResponse(f'<h1>Текущее время</h1>{now}')
    response = render(request, "core/index.html", context={'dt': now})
    return response
