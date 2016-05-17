# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Service
from category.serializers import CategoryHyperlinkedSerializer


class ServiceListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Service
        fields = ('id', 'url', 'title', 'capture', 'category')


class ServiceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Service
