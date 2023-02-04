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
        request = self.request
        user_id = request.user.id
        try:
            raiser_id = Profile.objects.get(user_id=user_id)
            print('\n\n\n')
            print(raiser_id)
            print('\n\n\n')
        except:
            pass
        return {"raiser_id": raiser_id}


class ProfileViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        return {"user_id": self.request.user.id}

    # def get_permissions(self):
    #     if self.request.method in permissions.SAFE_METHODS:
    #         return [permissions.IsAuthenticated()]
    #     elif self.request.method == 'POST':
    #         return [permissions.IsAuthenticated()]
    #     else:
    #         return [permissions.IsAdminUser()]

    # @action(detail=False, methods=['GET', 'PUT'], permission_classes=[permissions.IsAuthenticated])
    # def me(self, request: HttpRequest):

    #     (profile, created) = Profile.objects.get_or_create(
    #         user_id=request.user.id
    #     )

    #     if request.method == 'GET':
    #         serializer = UserProfileSerializer(profile)
    #     elif request.method == 'PUT':
    #         serializer = UserProfileSerializer(profile, data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()

    #     return Response(serializer.data)
