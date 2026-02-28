from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(default="")
    author_name = models.CharField()
    content = models.CharField(max_length=8192)

    def get_absolute_url(self):
        return reverse("post", kwargs={"pk": str(self.pk)})

    class Meta:
        ordering = ['pk']

class Reply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=8192)
    author_name = models.CharField()

    def get_absolute_url(self):
        return reverse("post", kwargs={"pk": str(self.post.pk)})