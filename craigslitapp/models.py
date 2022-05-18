from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=128, default="")
    author = models.CharField(max_length=128, default="")
    description = models.TextField(default="")
    price = models.FloatField(default=0)
    location = models.CharField(max_length=128, default="")
    condition = models.CharField(max_length=128, default="")
    size = models.CharField(max_length=128, default="")
    notes = models.CharField(max_length=128, default="")
    created = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.title
