from .models import Profile,BloodStock
from .serializer import ProfileSerializer,BloodStockSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .permissions import IsActivatedOrReadOnly,IsAdmin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import get_user_model, login
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
import requests
from django.contrib.sites.shortcuts import get_current_site
from rest_framework_simplejwt.tokens import RefreshToken


class ProfileList(APIView):
    # permission_classes = (IsAuthenticated,)

    def get_user(self, request):
        
        try:
            user_id = request.GET.get('user_id')
                
            return User.objects.filter(id = user_id).first()
        except User.DoesNotExist:
            raise Http404()

    def get_profile(self, pk):
        try: 
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404


    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    
class BloodStockList(APIView):
    # permission_classes = (IsAdmin)

    def get_blood(self, pk):
        try: 
            return BloodStock.objects.get(pk=pk)
        except BloodStock.DoesNotExist:
            return Http404

    def get(self, request, format=None):
        all_bloodstock = BloodStock.objects.all()
        serializers = ProfileSerializer(all_bloodstock, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = BloodStockSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    


    

    












    





