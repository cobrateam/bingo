from django.contrib.admin import site

from post.models import Post

site.register(Post)
