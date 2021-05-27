from django.db import models
from django.db.models import fields
from rest_framework import serializers

# imported models
from .models import Notice, Record, Match

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = "__all__"

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ["id","first_name", "last_name", "province","dat_of_birth"]

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = "__all__"