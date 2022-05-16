from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=128, default="")
    author = models.CharField(max_length=128, default="")
    description = models.TextField(default="")
    price = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.title
