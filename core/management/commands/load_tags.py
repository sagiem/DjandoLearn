from django.core.management.base import BaseCommand
from urllib.parse import urljoin
from django.conf import settings
import requests


class Command(BaseCommand):
    help = 'Пример загрузки данных через REST API'

    def add_arguments(self, parser):
        parser.add_argument('--username', '-u', dest='username', help='Имяпользователя')
        parser.add_argument('--password', '-p', dest='password')


    def handle(self, *args, **options):
        login_url = urljoin(settings.MY_EXETNAL_SERVICE, '/register')
        response = requests.post(login_url, data={
            'username': options['username'],
            'password': options['password'],
        })
        response.raise_for_status()

        login_result = response.json()
        print(login_result)


