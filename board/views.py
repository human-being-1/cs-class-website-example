from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from .models import Subforum, Post

# Create your views here.

class AllSubforumsView(ListView):
    model = Subforum
    template_name = "index.html"

class SubforumView(DetailView):
    model = Subforum
    template_name = "subforum.html"

class CreatePostView(CreateView):
    model = Post
    fields = ["title", "content", "author_name"]
    template_name = "create_post.html"