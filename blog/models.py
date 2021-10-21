from django.db import models
from django.db.models.deletion import CASCADE
from django.urls.base import reverse

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
            return f"{self.caption}"

class Post(models.Model):
    image_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    date = models.DateField()
    content = models.TextField()
    slug = models.SlugField(default="", null=False, db_index=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse("post-detail-page", args=[self.slug])

    def __str__(self):
        return f"{self.title} by {self.author} - {self.date}"
