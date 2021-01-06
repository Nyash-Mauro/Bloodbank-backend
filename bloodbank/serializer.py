from rest_framework import serializers
from .models import *
from .models import Profile,BloodStock

class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = '__all__'

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donations
        fields = '__all__


class ProfileSerializer(serializers.ModelSerializer):
     class Meta:
        model = Profile
        fields= '__all__'


class BloodStockSerializer(serializers.ModelSerializer):
     class Meta:
        model = BloodStock
        fields= '__all__'

