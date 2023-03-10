from rest_framework import serializers
from core import models

class Tag(serializers.ModelSerializer):
    display  = serializers.SerializerMethodField()
    class Meta:
        model = models.Tag
        fields = '__all__'

    def get_display(self, obj: models.Tag) -> str:
        return  f'{obj.id}. {obj.name}'

class tagSearch(serializers.Serializer):
    name = serializers.CharField(label='Название', required=True)

    def validate_name(self, value):
        if not models.Tag.objects.filter(name__icontains=value):
            raise serializers.ValidationError(f'Нет меток содержащих название "{value}"')
        return value

    def validate(self, attrs):
        return attrs
