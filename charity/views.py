from django.shortcuts import render
from django.http import HttpRequest
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Advertisement, DonatorDonate
from .serializers import AdvertisementSerializer, UserProfileSerializer


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer


class DonatorDonateeViewSet(ModelViewSet):
    queryset = DonatorDonate.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAdminUser]

    # def get_permissions(self):
    #     if self.request.method in permissions.SAFE_METHODS:
    #         return permissions.IsAuthenticated()

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[permissions.IsAuthenticated])
    def me(self, request: HttpRequest):

        (profile, created) = DonatorDonate.objects.get_or_create(
            user_id=request.user.id
        )
        print('hi\n\n\n')
        if request.method == 'GET':
            serializer = UserProfileSerializer(profile)
        elif request.method == 'PUT':
            serializer = UserProfileSerializer(profile, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        return Response(serializer.data)
