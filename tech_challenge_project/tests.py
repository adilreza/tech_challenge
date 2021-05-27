import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from src.tech_challenge_app.models import Hello

class HelloTestCase(APITestCase):

    def test_helloworld(self):
        data = {"name": "adil5555"}
        response  = self.client.post('/api/v1/ping/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    def test_hello2(self):
        data = {"name": "adil5555"}
        url = "/api/v1/ping/"
        response  = self.client.post(url, data)
        self.assertEqual(Hello.objects.count(),1)