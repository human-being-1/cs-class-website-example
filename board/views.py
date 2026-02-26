from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Subforum, Post

# Create your views here.

class AllSubforumsView(ListView):
    model = Subforum
    template_name = "index.html"

class SubforumView(DetailView):
    model = Subforum
    template_name = "subforum.html"