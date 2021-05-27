import json
from src.tech_challenge_app.models import Record, Notice, Match
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class HelloTestCase(APITestCase):

    def test_record(self):
        data = {"first_name":"adil", "last_name":"reza","province":"Ok","dat_of_birth":"1997-01-12"}
        url = "/api/v1/record/"
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Record.objects.count(), 1)

    def test_notice(self):
        data = {"first_name":"adil", "last_name":"reza","province":"Ok","dat_of_birth":"1997-01-12", "alt_first_name":"leo"}
        url = "/api/v1/notice/"
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["alt_first_name"], "leo")
        self.assertEqual(Notice.objects.count(), 1)
    
    # def test_match(self):
    #     data = {"first_name":"adil", "last_name":"reza","province":"Ok","dat_of_birth":"1997-01-12", "alt_first_name":"leo"}
    #     url = "/api/v1/notice/"
    #     response1 = self.client.post(url, data)
    #     url2 = f"/api/v1/record/{response1.data['id']}"
    #     response11 = self.client.get(url2)

    #     data = {"first_name":"adil", "last_name":"reza","province":"Ok","dat_of_birth":"1997-01-12"}
    #     url = "/api/v1/record/"
    #     response2 = self.client.post(url, data)
    #     url3 = f"/api/v1/record/{response2.data['id']}"
    #     response22 = self.client.get(url3)
    #     print(response22)

    #     url = "/api/v1/match/"
    #     data = {"notice":response11.data, "record":response22.data, "type":1}

    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)


