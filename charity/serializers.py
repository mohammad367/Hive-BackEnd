from rest_framework import serializers
from charity.models import Advertisement, Profile


class AdvertisementSerializer(serializers.ModelSerializer):
    raiser_id = serializers.SerializerMethodField(
        read_only=True, method_name='get_raiser_id')
    print('\n\n\nhi\n\n\n')

    def get_raiser_id(self):
        print('hi\n\n\n\n')
        return self.context['raiser_id']

    class Meta:
        model = Advertisement
        fields = ['id', 'raiser_id', 'title',
                  'description', 'amount', 'collected_amount']


class UserProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(
        read_only=True)

    class Meta:
        model = Profile
        # add all fields included in user profile design
        fields = ['id', 'user', 'first_name', 'last_name',
                  'account_number', 'birth_date', 'identity_card_image']
