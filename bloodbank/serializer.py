from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    @staticmethod
    def validate_password(password: str) -> str:
        return make_password(password)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','role','is_admin','is_staff','is_active','password')

    # def update(self, instance, validated_data):
    #     password = validated_data.pop('password', None)

    #     for (key, value) in validated_data.items():
    #         setattr(instance, key, value)

    #     if password is not None:
    #         instance.set_password(password)
    #         instance.save()

    #     return instance




class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','role','is_admin','is_staff','is_active','password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'], validated_data['password'])

        return user


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)