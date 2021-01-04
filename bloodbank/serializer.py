from rest_framework import serializers
from .models import Profile,BloodStock

class ProfileSerializer(serializers.ModelSerializer):
     class Meta:
        model = Service
        fields= '__all__'
