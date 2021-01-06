from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
from knox import views as knox_views
router = DefaultRouter()

# router.register('api/user', UserViewSet)



# urlpatterns = [
#     path('user/', RegistrationAPIView.as_view(),name='RegistrationAPIView'),
#     path('user/login/', LoginAPIView.as_view(),name='LoginAPIView'),
#     path('user/', UserRetrieveUpdateAPIView.as_view(),name='UserRetrieveUpdateAPIView'),
#     path('',include(router.urls))
    
# ]


urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/user/', UserAPI.as_view(), name='user'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('',include(router.urls))

]