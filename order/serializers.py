# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Order
from account.serializers import AccountDetailSerializer


class OrderListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'url', 'service', 'price', 'date')


class OrderDetailSerializer(serializers.ModelSerializer):

    account = AccountDetailSerializer(read_only=True)
    staff = AccountDetailSerializer(read_only=True)

    service = serializers.HyperlinkedRelatedField(
        view_name = 'service-detail',
        read_only = True
    )

    class Meta:
        model = Order
        fields = ('id', 'url', 'account', 'service', 'staff', 'price', 'date')
