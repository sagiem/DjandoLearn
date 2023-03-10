from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Item(models.Model):
    user = models.ForeignKey(User, verbose_name='Поьзователь', on_delete=models.CASCADE, related_name='items')
    name = models.CharField('Название', max_length=255, blank=True, unique=True)
    description = models.TextField('Описание', help_text='подсказка, если применимо')
    priority = models.IntegerField('Приоритет сортировки', default=1, db_index=True)
    done = models.DateTimeField('Выполено', null=True, blank=True)
    created = models.DateTimeField('Создан', auto_now_add=True, db_index=True)
    updated = models.DateTimeField('Обновлен', auto_now=True)
    tags = models.ManyToManyField(Tag, verbose_name='Метки', blank=True, related_name='items')

    class Meta:
        verbose_name = 'Дело'
        verbose_name_plural = 'Список дел'
        ordering = ('priority', 'created')

    def __str__(self):
        return self.name







