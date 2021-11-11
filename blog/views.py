from django.shortcuts import get_object_or_404, render
from django.urls.base import reverse

from django.views.generic import ListView, DetailView

from .models import Post
# Create your views here.


class IndexPostsListView(ListView):
    template_name = "blog/index.html"
    model = Post

    context_object_name = "posts"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.order_by("-date")[:3]
        return data


class AllPostsListView(ListView):
    template_name = "blog/posts.html"
    model = Post

    context_object_name = "posts"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.order_by("-date")
        return data


class PostDetailView(DetailView):
    template_name = "blog/post.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
