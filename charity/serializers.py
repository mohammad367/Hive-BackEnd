from rest_framework import serializers
from charity.models import Advertisement, DonatorDonate


class AdvertisementSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False)
    class Meta:
        model = Advertisement
        fields = ['raiser', 'title', 'description',
                  'amount', 'collected_amount']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonatorDonate
        # add all fields included in user profile design
        fields = ['user', 'account_number']
