from djoser.serializers import UserCreateSerializer as BaseUserSerializer
from djoser.email import ActivationEmail
# 'activation': 'djoser.serializers.ActivationSerializer',
from djoser.serializers import ActivationSerializer


class UserCreateSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'email', 'username',
                  'password', 'first_name', 'last_name']
