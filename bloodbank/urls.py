from django.urls import path,include
from .views import ConditionSetView,DonationSetView,ProfileList,BloodStockList
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from . import views
from .views import *



router = DefaultRouter()
router.register("condition",ConditionSetView)
router.register("donations",DonationSetView)

# urlpatterns=[
#     path('',views.index,name='index'),
# ] + router.urls

urlpatterns = [
    path('api/v1/profiles/', views.ProfileList.as_view(), name='profile_add'),
    path('api/v1/bloodstocks/', views.BloodStockList.as_view(), name='bloodstock_info'),
    path('api/v1/profile/<int:pk>/', views.ProfileItem.as_view(), name='profile_edit'),
    path('api/v1/bloodstock/<int:pk>/', views.BloodStockItem.as_view(), name='bloodstock_edit'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/logout/', TokenRefreshView.as_view(), name='logout'),
    path('users/', views.UserViewSet.as_view()),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/',include(router.urls)),

]
