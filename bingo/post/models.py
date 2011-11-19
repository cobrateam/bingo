from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ("post_detail", [self.id])
