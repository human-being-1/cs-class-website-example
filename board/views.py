from django.shortcuts import render
from django.views.generic import ListView
from .models import Subforum, Post

# Create your views here.

class SubforumsView(ListView):
    model = Subforum
    template_name = "index.html"