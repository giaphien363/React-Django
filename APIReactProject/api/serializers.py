from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.views import Token

from .models import articles


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = articles
        fields = ['id', 'title', 'description']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

        extra_kwargs = {'password': {
            'required': True,
            'write_only': True
        }}

    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        Token.objects.create(user=user)
        return user
