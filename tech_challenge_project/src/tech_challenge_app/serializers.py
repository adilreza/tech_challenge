from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import Hello

class HelloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hello
        fields = "__all__"