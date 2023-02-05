from rest_framework import serializers
from charity.models import Advertisement, Profile
from django.conf import settings
from uuid import uuid4


class UserBasicSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'first_name', 'last_name']
        read_only = ['first_name', 'last_name']


class AdvertisementSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(
        read_only=True)

    raiser_id = serializers.ReadOnlyField(source='profile.username')

    # raiser_id = serializers.UUIDField(read_only=True)
    # raiser = UserBasicSerializer(read_only=True)
    # print('\n\n\nhi\n\n\n')

    # def get_raiser_id(self):
    #     print('hi\n\n\n\n')
    #     return self.context['raiser_id']
    # raiser = serializers.PrimaryKeyRelatedField(read_only=True)
    # def get_raiser_id(self, advetisement):
    #     print('\n\n\n\n\n')
    #     user_id = self.context['request'].user.id
    #     print(user_id)
    #     print('\n\n')
    #     return user_id

    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'raiser_id',
                  'description', 'amount', 'collected_amount']


class UserProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Profile
        # add all fields included in user profile design
        fields = ['id', 'user', 'first_name', 'last_name',
                  'account_number', 'birth_date', 'identity_card_image']
        read_only = ['user']
