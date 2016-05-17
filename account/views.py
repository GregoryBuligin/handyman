from django.shortcuts import render
from django.http import Http404

from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import viewsets

from .permissions import IsOwnerOrReadOnly
from .models import Account
from .serializers import (
    AccountDetailSerializer,
    AccountListSerializer,
    AccountCreateSerializer
)

# Create your views here.

class CreateAccountView(generics.CreateAPIView):
    """
    Создание аккаунта

    Представление, позволяющее создать аккаунт с
    уровнем разрешения: для всех пользователей.

    """
    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer
    permission_classes = (permissions.AllowAny,)


class AccountViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    """
    Просмотр информации об аккаунтах.

    Просмотр списка, конкретного аккаунта,
    обновления информации (если пользователь является
    владельцем выбраного для изменения аккаунта).

    """
    queryset = Account.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return AccountListSerializer
        else:
            return AccountDetailSerializer


class OwnerAPIView(APIView):
    """
    Данные о текущем пользователе.

    Позволяет просмотреть информацию о пользователе,
    прошедшем аутентификацию, изменить данные.

    """
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        if request.user:
            owner = self.get_object(request.user.pk)
            # print(request.user.pk)
            serializer = AccountDetailSerializer(owner)
            return Response(serializer.data)

    def put(self, request, format=None):
        if request.user:
            owner = self.get_object(request.user.pk)
            serializer = AccountDetailSerializer(owner, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
