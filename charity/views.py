from django.shortcuts import render
from django.http import HttpRequest
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Advertisement, Profile
from .serializers import AdvertisementSerializer, UserProfileSerializer


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    def get_serializer_context(self):
        return {"request": self.request}
    # def get_serializer_context(self):
    #     request = self.request
    #     user_id = request.user.id
    #     try:
    #         raiser_id = Profile.objects.get(user_id=user_id)
    #         print('\n\n\n')
    #         print(raiser_id)
    #         print('\n\n\n')
    #     except:
    #         pass
    #     return {"raiser_id": raiser_id}


class ProfileViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer
