from django.contrib import admin
from core import models

# Register your models here.
@admin.register(models.Person)
class Person(admin.ModelAdmin):
    list_display = ('name', 'phone')
    search_fields = ('name',)
