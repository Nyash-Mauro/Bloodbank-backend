from rest_framework import serializers
from .models import Profile,BloodStock

class ProfileSerializer(serializers.ModelSerializer):
     class Meta:
        model = Profile
        fields= '__all__'

class BloodStockSerializer(serializers.ModelSerializer):
     class Meta:
        model = BloodStock
        fields= '__all__'


