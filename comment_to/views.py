from django.shortcuts import render

from rest_framework import mixins
from rest_framework import viewsets

from django_comments.models import Comment

from .serializers import (
    CommentListSerializer,
    CommentDetailSerializer
)

# Create your views here.

class CommentViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    """
    Просмотр комментариев

    Создание, посмотр, просмотр списка
    комментариев.

    """
    queryset = Comment.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CommentListSerializer
        else:
            return CommentDetailSerializer
