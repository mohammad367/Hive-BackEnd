from django.urls import path, include
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register(r'advertisements', views.AdvertisementViewSet,
                 basename='advertisements')


urlpatterns = [
    path('', include(routers.urls))
]
