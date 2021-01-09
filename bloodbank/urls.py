from django.urls import path,include
from .views import *
from . import views
from rest_framework.routers import DefaultRouter
from knox import views as knox_views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/logout/', TokenRefreshView.as_view(), name='logout'),
    path('users/', views.UserViewSet.as_view()),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    # path('api/user/', UserAPI.as_view(), name='user'),
    # path('api/login/', LoginAPI.as_view(), name='login'),
    # path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    # path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('',include(router.urls))

]