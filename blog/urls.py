from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:post_title_url>", views.post, name="post")
]
