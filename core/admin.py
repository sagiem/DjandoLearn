from django.contrib import admin
from core import models

class ItemResultInLine(admin.TabularInline):
    model = models.ItemResult



@admin.register(models.Item)
class Item(admin.ModelAdmin):
    inlines = (ItemResultInLine, )
    list_display = ('name', 'done')
    search_fields = ('name',)

# @admin.register(models.Tag)
# class Tag(admin.ModelAdmin):
#     inlines = (ItemResultInLine, )
#     list_display = ('name', 'done')
#     search_fields = ('name',)


# @admin.register(models.Person)
# class Person(admin.ModelAdmin):
#     list_display = ('name', 'phone')
#     search_fields = ('name',)
