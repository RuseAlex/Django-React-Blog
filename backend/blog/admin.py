from django.contrib import admin
from .models import Post, Comment

List = [Post, Comment]


admin.site.register(List)
