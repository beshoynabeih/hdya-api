from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import User


class UserCreateSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        model = User
        field = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'mobile',
            'avatar',
            'birth_date',
            'address',
            'password'
        )