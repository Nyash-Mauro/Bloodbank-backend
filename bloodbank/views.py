from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import RecipientsSerializer
from rest_framework import viewsets
from .models import Recipients



class RecipientsViewSet(viewsets.ModelViewSet):
    queryset = Recipients.objects.all()
    serializer_class = RecipientsSerializer