from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from .models import Post, Reply

# Create your views here.

class AllPostsView(ListView):
    model = Post
    template_name = "index.html"

class PostView(DetailView):
    model = Post
    template_name = "post.html"

class CreatePostView(CreateView):
    model = Post
    fields = ["title", "content", "author_name"]
    template_name = "create_post.html"

class CreateReplyView(CreateView):
    model = Reply
    fields = ["content", "author_name"]
    template_name = "create_reply.html"
    pk = 0

    def form_valid(self, form):
        form.instance.post = Post.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)