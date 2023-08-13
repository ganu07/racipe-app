"""
Serializers for the user API
"""

from django.contrib.auth import (
    get_user_model,
    authenticate
    )
from django.utils.translation import gettext as _
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """ Serializer for user object"""

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """create and return user with encrypcted password"""
        return get_user_model().objects.create_user(**validated_data)


class AuthToeknSerializer(serializers.Serializer):
    """ Serializer for the user auth"""

    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """ validate and authenticate user"""
        email = attrs.get('email')
        password  = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )

        if not user:
            msg = _('unable t authenticate with provide credentials')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

    def update(self, instance, validated_data):
        """ update and return user"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user
