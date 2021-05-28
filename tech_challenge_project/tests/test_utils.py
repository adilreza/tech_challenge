from src.tech_challenge_app.utils import strong_match, possible_match, weak_match
from src.tech_challenge_app.models import Record, Notice
from rest_framework.test import APITestCase
from rest_framework import status

class UtilTestCase(APITestCase):

    def test_strong(self):
        data = {"first_name":"Lionel", "last_name":"Messi", "alt_first_name":"Leo","province":"ON","dat_of_birth":"1997-01-12"}
        url = "/api/v1/notices"
        self.response = self.client.post(url, data)

        self.assertEqual(self.response.status_code, 301)
        self.assertEqual(strong_match("Lionel", "Messi", "1997-01-12"), 0)
    
    def test_possible(self):
        data = {"first_name":"Lionel", "last_name":"Messi", "alt_first_name":"Leo","province":"ON","dat_of_birth":"1997-01-12"}
        url = "/api/v1/notices"
        self.response = self.client.post(url, data)

        self.assertEqual(self.response.status_code, 301)
        self.assertEqual(possible_match("Lionel", "Messi", "ON"), 0)
    
    def test_weak(self):
        data = {"first_name":"Lionel", "last_name":"Messi", "alt_first_name":"Leo","province":"ON","dat_of_birth":"1997-01-12"}
        url = "/api/v1/notices"
        self.response = self.client.post(url, data)

        self.assertEqual(self.response.status_code, 301)
        self.assertEqual(weak_match("Lionel", "Messi"), 0)