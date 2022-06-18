from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.generics import (RetrieveDestroyAPIView, ListCreateAPIView,
                                     CreateAPIView)
from .serializers import PostListSerializer, PostDetailSerializer, CommentSerializer
from .models import Post
from .paginators import FasterPageNumberPagination
from .permissions import PostDestroyPermission


class PostListView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = PostListSerializer
    queryset = Post.objects.order_by('-created_at').prefetch_related('author')
    pagination_class = FasterPageNumberPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentCreationView(CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        from .models import Post

        post = Post.objects.get(id=self.kwargs['pk'])
        user = self.request.user
        serializer.save(author=user, post=post)


class PostDetailView(RetrieveDestroyAPIView):
    permission_classes = [PostDestroyPermission, ]
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all().prefetch_related('author')
