from djoser.serializers import UserCreateSerializer as BaseUserSerializer

class UserCreateSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields=['id','email','username','password','first_name','last_name']