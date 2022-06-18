from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model


User = get_user_model()


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)

    class Meta:
        model = Post
        fields = ['title', 'author', 'content', 'created_at']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)
    post_id = serializers.CharField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class PostDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
