from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets,generics
from . import models
from . import serializer
from .models import Condition,Donations
from .serializer import ConditionSerializer,DonationSerializer
from django.contrib.auth import get_user_model, login


def index(request):
    return render(request,'home.html')

class ConditionSetView(viewsets.ModelViewSet):
    queryset = models.Condition.objects.all()
    serializer_class = ConditionSerializer

class DonationSetView(viewsets.ModelViewSet):
    queryset = models.Donations.objects.all()
    serializer_class = DonationSerializer
    
