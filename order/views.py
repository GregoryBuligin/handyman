from django.shortcuts import render

from rest_framework import mixins
from rest_framework import viewsets

from .models import Order
from .serializers import (
    OrderListSerializer,
    OrderDetailSerializer
)

# Create your views here.

class OrderViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    """
    Информация о заказе.

    Позволяет просмотреть данные о заказе,
    список заказов, создать новый заказ.

    """
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return OrderListSerializer
        else:
            return OrderDetailSerializer
