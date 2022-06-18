from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

def get_deleted_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Post(models.Model):
    title = models.CharField(max_length=70)
    author = models.ForeignKey(User, on_delete=models.SET(get_deleted_user))
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.author}'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET(get_deleted_user))
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post.title} ({self.id}) - {self.author}'

