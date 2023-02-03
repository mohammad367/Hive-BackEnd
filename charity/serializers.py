<<<<<<< HEAD


# AdvertisementSerializer:

# amount
# collected_amount
# title
# description
# raiser-> serializer///
# photo


# DonatorDonateeSerializer:
# user-id
# birth_date
# is_verified default=false
# identity_code *
# account_number *
# postal_code */
# identity_cart_photo */
# identity_cart_photo1 */


# UserProfileSerializer:
# user-id
# birth_date
# is_verified default=false
# identity_code *
# account_number *
# postal_code */
# identity_cart_photo */
# identity_cart_photo1 */
=======
from rest_framework import serializers
from charity.models import Advertisement, DonatorDonate


class AdvertisementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advertisement
        fields = ['raiser', 'title', 'description',
                  'amount', 'collected_amount']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonatorDonate
        # add all fields included in user profile design
        fields = ['user', 'account_number']
>>>>>>> 636b17f83957256000cfd3334525863a3f417df6
