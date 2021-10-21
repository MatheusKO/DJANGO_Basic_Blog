from django.contrib import admin

from .models import Author, Tag, Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
  # readonly_fields = ("slug", )
  prepopulated_fields = {"slug": ("title", )}
  list_filter = ("author", )
  list_display = ("title", "author", "date")

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)