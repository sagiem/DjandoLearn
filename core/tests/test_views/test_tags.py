from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework import status

from core import models, factories


class Tag(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = models.User.objects.create_user(username='test', password='123')
        self.token = Token.objects.create(user=self.user)


    def test_anonymuos_deny(self):
        response = self.client.get(reverse('core:tag-list'))
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_list_ok(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        factories.Tag()
        response = self.client.get(reverse('core:tag-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Tag.objects.count(), len(response.data))

