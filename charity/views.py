from django.shortcuts import render
from charity.serializers import *
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.


class AdvertisementViewSet(ModelViewSet):
    serializer_class =AdvertisementSerializer() 
    # parser_classes = (MultiPartParser, FormParser)

    # def perform_create(self, serializer):
    #     serializer.save(creator=self.request.user)
    pass


class DonatorDonateeViewSet(ModelViewSet):
    # serializer_class =UserProfileSerializer()

    # parser_classes = (MultiPartParser, FormParser)

    # def perform_create(self, serializer):
    #     serializer.save(creator=self.request.user)
    pass
