
from django.urls import path, re_path
from . import views
from .views import ConditionSetView,DonationSetView,ProfileList,BloodStocklist
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
from . import views


router = DefaultRouter()
router.register(r"condition",ConditionSetView)
router.register(r"donations",DonationSetView)

urlpatterns=[
    path('',views.index,name='index'),
] + router.urls

urlpatterns = [
    path('',views.index,name='index'),
    path('api/v1/profiles/', views.ProfileList.as_view(), name='profile_add'),
    path('api/v1/profile/<int:pk>/', views.ProfileList.as_view(), name='profile_edit'),
    path('api/v1/bloodstocks/', views.BloodStockList.as_view(), name='bloodstock_info'),
    path('api/v1/bloodstock/<int:pk>', views.ProfileList.as_view(), name='bloodstock_edit'),




if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)