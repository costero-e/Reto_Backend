import string
from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'url', 'body', 'created_at', 'published', 'username']
