from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets




# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(
#         max_length=128,
#         min_length=8,
#         write_only=True
#     )

#     class Meta:
#         model = User
#         fields = ('email','first_name','last_name','is_admin','is_staff','is_active','role','password')

#     def update(self, instance, validated_data):
#         password = validated_data.pop('password', None)

#         for (key, value) in validated_data.items():
#             setattr(instance, key, value)

#         if password is not None:
#             instance.set_password(password)
#             instance.save()

#         return instance

    
# class RegistrationSerializer(serializers.ModelSerializer):
#     """Serializers registration requests and creates a new user."""

#     password = serializers.CharField(
#         max_length=128,
#         min_length=8,
#         write_only=True
#     )

#     class Meta:
#         model = User
#         fields = ['email', 'password', 'token']

#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)


# class LoginSerializer(serializers.Serializer):
#     email = serializers.CharField(max_length=255)
#     # username = serializers.CharField(max_length=255, read_only=True)
#     password = serializers.CharField(max_length=128, write_only=True)

#     def validate(self, data):
#         email = data.get('email', None)
#         password = data.get('password', None)

#         if email is None:
#             raise serializers.ValidationError(
#                 'Please enter email address.'
#             )

#         if password is None:
#             raise serializers.ValidationError(
#                 'A password is required to log in.'
#             )
#         user = authenticate(email=email, password=password)

#         if user is None:
#             raise serializers.ValidationError(
#                 'A user with this email and password was not found.'
#             )
#         if not user.is_active:
#             raise serializers.ValidationError(
#                 'This user has been deactivated.'
#             )
#         return {
#             'email': user.email,
#             # 'username': user.username,

#         }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','role','is_admin','is_staff','is_active')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','role','is_admin','is_staff','is_active','password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user( validated_data['email'], validated_data['password'])

        return user