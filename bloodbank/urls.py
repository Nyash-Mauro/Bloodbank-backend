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
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url
schema_view = get_schema_view(
   openapi.Info(
      title="Bloodbank_Management_System API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()
router.register("condition",ConditionSetView)
router.register("donations",DonationSetView)

# urlpatterns=[
#     path('',views.index,name='index'),
# ] + router.urls

urlpatterns = [
    path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
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
