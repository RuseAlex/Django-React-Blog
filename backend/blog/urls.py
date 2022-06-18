from django.urls import path, include
from .views import PostListView, PostDetailView, CommentCreationView


urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('posts/', PostListView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()),
    path('posts/<int:pk>/comments/', CommentCreationView.as_view()),
]
