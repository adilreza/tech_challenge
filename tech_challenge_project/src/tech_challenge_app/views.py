from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from django.http import Http404
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

    def get_object(self, pk):
        try:
            return Record.objects.get(pk=pk)
        except Record.DoesNotExist:
            raise Http404

    # def get(self, request, format=None):
    #     data = Record.objects.values()
    #     data_list = list(data)
        
    #     return JsonResponse({"record":data_list})
    
    # def get(self, request, pk, format=None):
    #     data = Record.objects.filter(pk=pk).values()
    #     data_list = list(data)
    #     return JsonResponse({"record":data_list})

    
    def post(self, request, format=None):
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
        
    def delete(self, request, pk, format=None):
        pk2 = int(pk)
        data = Match.objects.filter(pk=pk2)
        for sdata in data:
            r_id = sdata.record.id
            n_id = sdata.notice.id
        Match.objects.filter(pk=pk2).delete()
        Record.objects.filter(pk=r_id).delete()
        return JsonResponse({"message":"deleted_successfully"})
