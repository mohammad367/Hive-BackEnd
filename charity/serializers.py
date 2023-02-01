from rest_framework import serializers
from charity.models import Advertisement , DonatorDonate

class AdvertisementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advertisement
        fields = ['raiser' ,'title','description','amount','collected_amount']

class DonatorDonateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonatorDonate
        fields = ['donator','account_number']