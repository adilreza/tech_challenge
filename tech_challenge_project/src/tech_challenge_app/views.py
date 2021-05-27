from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from django.http import JsonResponse
import json
from .utils import match, update_match

from .models import Match, Record, Notice
from .serializers import NoticeSerializer, RecordSerializer
from .serializers import MatchSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    filter_backends  = (DjangoFilterBackend,)
    http_method_names = ['get',]

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    filter_backends  = (DjangoFilterBackend, )
    http_method_names = ['post','delete']

class NoticeSerializer(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    filter_backends  = (DjangoFilterBackend, )

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

        decision = match(first_name, last_name, province, date_of_birth)
        result = update_match(decision, first_name, last_name, province, date_of_birth)
        return JsonResponse({"message":"updated database"})
