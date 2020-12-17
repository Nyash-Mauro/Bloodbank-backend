from rest_framework import serializers
from .models import Recipients


class RecipientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipients
        fields = ('medical_facility','date_joined','location','blood_volume')
        
        
