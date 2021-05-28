import json
from src.tech_challenge_app.models import Record, Notice, Match
from rest_framework.test import APITestCase
from rest_framework import status

class ModelTestCase(APITestCase):

    def test_record(self):
        data = {"first_name":"adil", "last_name":"reza","province":"Ok","dat_of_birth":"1997-01-12"}
        url = "/api/v1/record/"
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Record.objects.count(), 1)

    def test_notice(self):
        data = {"first_name":"adil", "last_name":"reza","province":"Ok","dat_of_birth":"1997-01-12", "alt_first_name":"leo"}
        url = "/api/v1/notices/"
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["alt_first_name"], "leo")
        self.assertEqual(Notice.objects.count(), 1)
    
    def test_notice_400(self):
        data = {"first_name":[], "last_name":"reza","province":"Ok","dat_of_birth":"1997-01-12", "alt_first_name":"leo"}
        url = "/api/v1/notices/"
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 400)

    def test_record_400(self):
        data = {"first_name":[], "last_name":"reza","province":"Ok","dat_of_birth":"1997-01-12"}
        url = "/api/v1/record/"
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 400)

    def test_record_404(self):
        data = {"first_name":[], "last_name":"reza","province":"Ok","dat_of_birth":"1997-01-12"}
        url = "/api/v1/re"
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 404)

    def test_notice_404(self):
        data = {"first_name":"ok", "last_name":"reza","province":"Ok","dat_of_birth":"1997-01-12", "alt_first_name":"leo"}
        url = "/api/v1/not"
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 404)

    def test_match(self):
        data = {"first_name":"adil", "last_name":"reza","province":"ON","dat_of_birth":"1997-01-12", "alt_first_name":"leo"}
        url = "/api/v1/notices/"
        self.response1 = self.client.post(url, data)
        url2 = f"/api/v1/notices/{self.response1.data['id']}"
        print(url2)
        response11 = self.client.get(url2)

        data = {"first_name":"adil", "last_name":"reza","province":"Ok","dat_of_birth":"1997-01-12"}
        url = "/api/v1/record/"
        self.response2 = self.client.post(url, data)
        url3 = f"/api/v1/records/{self.response2.data['id']}"
        response22 = self.client.get(url3)

        url = "/api/v1/matches/"
        data33 = {"notice":response11, "record":response22, "type":1}

        response = self.client.post(url, data33)
        self.assertEqual(response.status_code, 405)

    def test_match_404(self):
        url = "/api/v1/matc"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


