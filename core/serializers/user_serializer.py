from rest_framework import serializers
from core.models.user_model import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'role')
        extra_kwargs = {'password': {'write_only': True}}


class CustomUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'role')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, clean_data):
        user_obj = CustomUser.objects.create_user(
            username=clean_data['username'], password=clean_data['password'])
        user_obj.username = clean_data['username']
        user_obj.save()
        return user_obj
