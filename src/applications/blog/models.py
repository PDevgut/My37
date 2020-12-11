import delorean
from django.db import models

def _now():
    return delorean.utcnow().datetime


class Post(models.Model):
    title = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    nr_likes = models.IntegerField(default=0)
    nr_views = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=_now)
    edited = models.BooleanField(default=False)
    class Meta:
        ordering = ["-created_at"]

class Comment(models.Model):
    article = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField("name author", max_length=50)
    text_comment = models.CharField("text comment", max_length=200)