import django_filters
from core import models


class Tag(django_filters.filterset.FilterSet):
    id = django_filters.NumberFilter(field_name='id')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        models = models.Tag
        fields = '__all__'


class Item(django_filters.filterset.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        models = models.Item
        fields = '__all__'