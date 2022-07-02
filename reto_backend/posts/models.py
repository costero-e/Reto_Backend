from django.db import models
from django.db.models import SET_NULL
from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    url = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    username = models.TextField()

    def __str__(self):
        return self.title
