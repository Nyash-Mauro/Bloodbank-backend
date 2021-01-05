from django.urls import path
from . import views
from .views import ConditionSetView,DonationSetView
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r"condition",ConditionSetView)
router.register(r"donations",DonationSetView)

urlpatterns=[
    path('',views.index,name='index'),
] + router.urls

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


