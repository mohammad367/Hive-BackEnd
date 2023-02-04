from rest_framework import serializers
from charity.models import Advertisement, Profile


class AdvertisementSerializer(serializers.ModelSerializer):
    raiser_id = serializers.IntegerField()

    class Meta:
        model = Advertisement
        fields = ['id', 'raiser_id', 'title',
                  'description', 'amount', 'collected_amount']


class UserProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Profile
        # add all fields included in user profile design
        fields = ['id', 'user_id', 'first_name', 'last_name',
                  'account_number', 'birth_date', 'identity_card_image']
