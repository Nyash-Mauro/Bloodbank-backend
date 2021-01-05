from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from .models import Profile,BloodStock

User = get_user_model()
