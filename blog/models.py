# blog/models.py

from django.db import models
from django.utils import timezone
# import user

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    # add author field

    def __str__(self):
        return self.title