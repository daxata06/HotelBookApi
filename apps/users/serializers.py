from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User


class UserRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()

    def create(self, **kwargs):
        validated_data = dict(list(self.validated_data.items()))
        if User.objects.filter(email=validated_data["email"]).exists():
            raise serializers.ValidationError("User with this email already exists")
        validated_data["password"] = make_password(validated_data["password"])
        validated_data["role"] = User.ROLE_CHOICES[0][0]
        return User.objects.create(**validated_data)
