from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from rest_framework import permissions

from . import models
from . import serializers


# Create your views here.

class ParticipantViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ParticipantProfileSerializer
    queryset = models.ParticipantProfile.objects.all()


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BookProfileSerializer
    queryset = models.BookProfile.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'author')


class IssueReturnViewSet(viewsets.ModelViewSet):
    """Handles getting a list of books issued to the employee and manages
    issue, re-issue, return of books."""

    serializer_class = serializers.IssueReturnSerializer
    queryset = models.BooksCurrentlyIssued.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('serial_no', 'employee_code')

class IssueReturnHistoryViewSet(viewsets.ModelViewSet):
    """Stores records of all book issue and return inside the system."""
    serializer_class = serializers.IssueReturnHistorySerializer
    queryset = models.BooksIssueReturnHistory.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('serial_no', 'employee_code')
