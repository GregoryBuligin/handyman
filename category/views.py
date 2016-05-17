# -*- coding: utf-8 -*-
from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Category
from .serializers import (
    CategoryHyperlinkedSerializer,
    CategoryListSerializer
)

# Create your views here.

class CategoryViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    """
    Просмотр и редактирование данных о категориях.

    Создание, посмотр, просмотр списка
    категорий.

    """
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CategoryListSerializer
        else:
            return CategoryHyperlinkedSerializer
