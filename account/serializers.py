# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Account


class AccountListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Account
        fields = ('id', 'url', 'username')


class AccountDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'updated_at',
            'email'
        )


class AccountCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        account = Account.objects.create_user(**validated_data)
        return account

    class Meta:
        model = Account
        fields = ('username', 'first_name', 'last_name', 'email',
            'username', 'password'
        )
        write_only_fields = ('password',)
