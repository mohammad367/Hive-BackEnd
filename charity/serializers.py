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
    class Meta:
        model = Advertisement
        fields = ['raiser_id', 'title', 'description',
                  'amount', 'collected_amount', 'category']


class AdvertisementCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(
        read_only=True)
    raiser_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'raiser_id', 'category',
                  'description', 'amount', 'collected_amount', 'image']

    def create(self, validated_data):
        user_id = self.context['request'].user.id
        # try:
        raiser_id = (Profile.objects.get(user_id=user_id).id)
        # raiser_id =
        # except:
        # pass
        # raise serializers.ValidationError(
        #     'this user does not has profile')
        print('\n\n', raiser_id)
        return Advertisement.objects.create(raiser_id=raiser_id, **validated_data)


class ProfileIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['raiser_id']


class UserProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(read_only=True)

    def create(self, validated_data):
        user_id = self.context['request'].user.id
        if Profile.objects.filter(user_id=user_id).exists():
            raise serializers.ValidationError('this user has profile')

        return Profile.objects.create(user_id=user_id, **validated_data)

    class Meta:
        model = Profile
        # add all fields included in user profile design
        fields = ['id', 'user_id', 'first_name', 'last_name',
                  'account_number', 'birth_date', 'identity_card_image']
