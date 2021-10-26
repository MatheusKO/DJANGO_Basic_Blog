from django.db import models
from django.db.models.deletion import CASCADE
from django.urls.base import reverse
from django.core.validators import MinLengthValidator

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.caption}"


class Post(models.Model):
    image_name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    content = models.TextField(validators=[MinLengthValidator(30)])
    slug = models.SlugField(null=False, unique=True)
    author = models.ForeignKey(
        Author, null=True, on_delete=models.SET_NULL, related_name="posts")
    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse("post-detail-page", args=[self.slug])

    def __str__(self):
        return f"{self.title} by {self.author} - {self.date}"
