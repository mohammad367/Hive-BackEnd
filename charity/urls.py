from django.urls import path, include
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register(r'advertisements', views.AdvertisementViewSet,
                 basename='advertisements')
routers.register(r'profile', views.UserProfileSerializer, basename='profile')

urlpatterns = [
    path('', include(routers.urls))
]
