from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import ProfileList


urlpatterns = [
    path('api/v1/profile/', views.ProfileList.as_view(), name='profile_edit'),

]