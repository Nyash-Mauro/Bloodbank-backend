from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .renderer import UserJSONRenderer
from .serializer import *
from .models import *
from django.contrib.auth import login
from rest_framework import permissions
from django.contrib.auth import get_user_model
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import generics, permissions
from django.views.decorators.debug import sensitive_post_parameters
from .models import Profile,BloodStock,User,Condition,Donations
from .serializer import ProfileSerializer,BloodStockSerializer,ConditionSerializer,DonationSerializer
from rest_framework.response import Response
# from rest_framework.views import APIView,generics
from rest_framework import viewsets
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
from . import models


class UserViewSet(APIView):
    def get(self, request, format=None):
        serializer = UserSerializer
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

class ProfileItem(APIView):
    # permission_classes = (IsAdminOrReadOnly,)
    def get_profile(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile, request.data,partial =  True)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail':'no profile with that user'}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        profile = self.get_profile(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
class BloodStockList(APIView):
    # permission_classes = (IsAdmin)

    def get_bloodstock(self, pk):
        try: 
            return BloodStock.objects.get(pk=pk)
        except BloodStock.DoesNotExist:
            return Http404

    def get(self, request, format=None):
        all_bloodstock = BloodStock.objects.all()
        serializers = BloodStockSerializer(all_bloodstock, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = BloodStockSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    
class BloodStockItem(APIView):
    # permission_classes = (IsAdminOrReadOnly,)
   
    def get_bloodstock(self, pk):
        try: 
            return BloodStock.objects.get(pk=pk)
        except BloodStock.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        bloodstock = self.get_bloodstock(pk)
        serializers = BloodStockSerializer(bloodstock)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        blood = self.get_bloodstock(pk)
        serializers = BloodStockSerializer(blood, request.data,partial =  True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        blood = self.get_bloodstock(pk)
        blood.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def index(request):
    #     return render(request,'home.html')

class ConditionSetView(viewsets.ModelViewSet):
        queryset = models.Condition.objects.all()
        serializer_class = ConditionSerializer

class DonationSetView(viewsets.ModelViewSet):
       queryset = models.Donations.objects.all()
       serializer_class = DonationSerializer

