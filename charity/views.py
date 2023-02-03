from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import permissions
from .models import Advertisement, DonatorDonate
from .serializers import AdvertisementSerializer, UserProfileSerializer


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer


class DonatorDonateeViewSet(ModelViewSet):
    queryset = DonatorDonate.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    @classmethod
    def user_test(self):
        print(self.request.user.user_permissions)
