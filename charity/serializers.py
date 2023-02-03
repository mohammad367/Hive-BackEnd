from rest_framework import serializers
from charity.models import Advertisement, DonatorDonate


class AdvertisementSerializer(serializers.ModelSerializer):
    raiser_id = serializers.IntegerField()

    class Meta:
        model = Advertisement
        fields = ['id', 'raiser_id', 'title',
                  'description', 'amount', 'collected_amount']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonatorDonate
        # add all fields included in user profile design
        fields = ['user', 'account_number']
