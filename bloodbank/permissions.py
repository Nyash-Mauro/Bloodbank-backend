from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from .models import Profile,BloodStock

User = get_user_model()

class IsActivatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_active


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_active

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff

