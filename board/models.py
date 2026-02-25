from django.db import models

# Create your models here.

class Subforum(models.Model):
    forum_name = models.CharField()
    description = models.CharField()

class Post(models.Model):
    subforum = models.ForeignKey(Subforum, on_delete=models.CASCADE, null=True)
    author_name = models.CharField()
    content = models.CharField(max_length=8192)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)