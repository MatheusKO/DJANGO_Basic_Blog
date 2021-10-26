from django.shortcuts import get_object_or_404, render
from django.urls.base import reverse

from .models import Post
# Create your views here.


def index(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]

    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/posts.html", {
        "posts": all_posts
    })


def post_detail(request, slug):

    post = get_object_or_404(Post, slug=slug)

    return render(request, "blog/post.html", {
        "title": post.title,
        "author": post.author,
        "date": post.date,
        "content": post.content,
        "image_name": post.image_name,
        "tags": post.tags.all()
        # TODO exhibit tags in post-detail-page
    })
