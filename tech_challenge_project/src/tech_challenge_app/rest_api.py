from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from .models import Hello
from .serializers import HelloSerializer

class HelloViewSet(viewsets.ModelViewSet):
    queryset = Hello.objects.all()
    serializer_class = HelloSerializer