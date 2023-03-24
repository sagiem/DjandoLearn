from django.test import TestCase
from core import models


class Tag(TestCase):

    def setUp(self):
        self.tag = models.Tag.objects.create(name='Купить молоко')

    def test_str(self):
        """Тестирование строкового представления объекта"""
        self.assertEqual(
            str(self.tag),
            self.tag.name,
            'Строковые кредставления должны браться из атрибута name'
        )