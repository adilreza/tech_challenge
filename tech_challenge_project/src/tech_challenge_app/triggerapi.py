from rest_framework.views import APIView
from django.http import JsonResponse
import json
import requests
from .utils import strong_match_fun, weak_match_fun, possible_match_fun, decision_maker, update_match_now

# imported model 
from .models import Notice





class RecordApi(APIView):
    def get(self, request):
        result = strong_match_fun("Lionel","Messi","1987-06-24")
        print(result)
        # json_data={"first_name":"Lionel", "last_name":"messi"}
        # province=""
        # date_of_birth=""
        # try:
        #     province = json_data["province"]
        # except KeyError:
        #     province="NOT"

        # try:
        #     date_of_birth = json_data["date_of_birth"]
        # except KeyError:
        #     date_of_birth="0000-00-00"
        # print(province, date_of_birth)
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

        # print("star working decission making-----------$$$$$$")

        decision = decision_maker(first_name, last_name, province, date_of_birth)

        result = update_match_now(decision, first_name, last_name, province, date_of_birth)
        return JsonResponse({"message":"updated database"})

        # if date_of_birth!="0000-00-00":
        #     result = strong_match_fun(first_name, last_name, date_of_birth)
        # elif province!="NOT":
        #     result = possible_match_fun(first_name, last_name, province)
        # elif date_of_birth=="0000-00--00" and province=="NOT":
        #     result = weak_match_fun(first_name, last_name)

        

        
