from rest_framework.views import APIView
from django.http import JsonResponse
import json
import requests
from .utils import decision_maker, update_match

# imported model 
from .models import Notice

class RecordApi(APIView):
    def get(self, request):
        return JsonResponse({"status":"OK working"})
    
    def post(self, request):
        json_data = json.loads(request.body)
        first_name = json_data["first_name"]
        last_name = json_data["last_name"]

        province=""
        date_of_birth=""
        try:
            province = json_data["province"]
        except KeyError:
            province="NOT"
        try:
            date_of_birth = json_data["date_of_birth"]
        except KeyError:
            date_of_birth="0000-00-00"

        decision = decision_maker(first_name, last_name, province, date_of_birth)

        result = update_match(decision, first_name, last_name, province, date_of_birth)
        return JsonResponse({"message":"updated database"})
