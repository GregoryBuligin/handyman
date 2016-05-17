# -*- coding: utf-8 -*-
from rest_framework import serializers

from django_comments.models import Comment


class CommentListSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='comment-detail')

    class Meta:
        model = Comment
        fields = ('id', 'url', 'user', 'submit_date')


class CommentDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
            'id',
            'comment',
            'user',
            'submit_date',
            'is_public',
            'is_removed'
        )
