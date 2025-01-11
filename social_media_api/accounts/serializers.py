from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token

# User registration serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'bio', 'profile_picture']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        Token.objects.create(user=user)  # Create a token for the new user
        return user

# User login serializer
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
