from django.db import models


class Item(models.Model):
    name = models.CharField('Название', max_length=255, blank=True)
    description = models.TextField('Описание', help_text='подсказка, если применимо')
    priority = models.IntegerField('Приоритет сортировки', default=1)
    bone = models.DateTimeField('Выполено', null=True, blank=True)
    create = models.DateTimeField('Создан', auto_now_add=True)
    update = models.DateTimeField('Обновлен', auto_now=True)

    class Meta:
        verbose_name = 'Дело'
        verbose_name_plural = 'Список дел'



class Person(models.Model):
    name = models.CharField('Имя', max_length=255)
    phone = models.IntegerField('Номер телефона')

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural ='Заказчики'

    def __str__(self):
        return self.name

