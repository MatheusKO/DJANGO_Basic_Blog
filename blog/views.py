from django.http.response import Http404
from datetime import date
from django.shortcuts import get_object_or_404, render
from django.urls.base import reverse

from .models import Post


def get_date(post):
    return post['date']

# Create your views here.


def index(request):
    blog_posts = Post.objects.all().order_by("-date")[:3]

    return render(request, "blog/index.html", {
        "posts": blog_posts
    })


def posts(request):
    posts = Post.objects.all().order_by("-date")
    return render(request, "blog/posts.html", {
        "posts": posts
    })


def post_detail(request, slug):

    post = get_object_or_404(Post, slug=slug)

    return render(request, "blog/post.html", {
        "title": post.title,
        "author": post.author,
        "date": post.date,
        "content": post.content,
        "image_name": post.image_name,
        "tags": post.tags
        # TODO exhibit tags in post-detail-page
    })
