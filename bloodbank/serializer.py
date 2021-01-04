from rest_framework import serializers
from .models import Profile,BloodStock

class ProfileSerializer(serializers.ModelSerializer):
     class Meta:
        model = Profile
        # fields = ['first_name','middle_name', 'last_name', 'email', 'age', 'gender', 'date_of_birth',
        #             'blood_group','phone_number','location','weight','date_registered']
        fields= '__all__'


class BloodStockSerializer(serializers.ModelSerializer):
     class Meta:
        model = BloodStock
        fields= '__all__'


