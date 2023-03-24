from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from core import models


class Register(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_not_allower(self):
        response = self.client.get(reverse('core:user_register'))
        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )
    def test_success_registration(self):
        data = {'username': 'test_user', 'password': '12345678'}
        response = self.client.post(path=reverse('core:user_register'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user = models.User.objects.filter(username=data['username']).first()
        self.assertTrue(user)
        self.assertTrue(user.check_password(data['password']))

