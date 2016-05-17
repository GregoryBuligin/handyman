# -*- coding: utf-8 -*-
import django_filters
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route

from .models import Service
from .serializers import ServiceSerializer, ServiceListSerializer



class ServiceViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    """
    Информация об услугах.

    Создание, посмотр, просмотр списка
    услуг.

    """
    queryset = Service.objects.all()
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('title', 'id')

    def get_serializer_class(self):
        if self.action == "list":
            return ServiceListSerializer
        else:
            return ServiceSerializer
