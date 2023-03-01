import django_filters
from core import models


class Tag(django_filters.filterset.FilterSet):
    id = django_filters.NumberFilter(field_name='id')
    term = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        models = models.Tag
        fields = '__all__'

