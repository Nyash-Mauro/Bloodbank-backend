from django.urls import path,include

from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('api/user', UserViewSet)



urlpatterns = [
    path('user/', RegistrationAPIView.as_view(),name='RegistrationAPIView'),
    path('user/login/', LoginAPIView.as_view(),name='LoginAPIView'),
    path('user/', UserRetrieveUpdateAPIView.as_view(),name='UserRetrieveUpdateAPIView'),
    path('',include(router.urls))
    
]