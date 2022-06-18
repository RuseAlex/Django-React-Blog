from rest_framework import serializers
from .models import Post, Comment


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
        fields = ['author', 'content', 'created_at', 'post_id']


class PostDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
