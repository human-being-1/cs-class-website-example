from django.db import models

# Create your models here.

class Subforum(models.Model):
    slug = models.SlugField(default="")
    forum_name = models.CharField()
    description = models.CharField()

    def __str__(self):
        return self.forum_name

class Post(models.Model):
    slug = models.SlugField(default="")
    subforum = models.ForeignKey(Subforum, on_delete=models.CASCADE, null=True)
    title = models.CharField(default="")
    author_name = models.CharField()
    content = models.CharField(max_length=8192)

class Reply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=8192)