from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters

from . import models
from . import serializers


# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BookProfileSerializer
    queryset = models.BookProfile.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'author')

