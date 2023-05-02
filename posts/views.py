from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post

                    #will give us a list of records of model
class PostListView(ListView):
    template_name = "posts/lists.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body"]