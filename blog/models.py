from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify

class Post(models.Model):
    """
    Model representing a blog post.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images', blank=True, null=True)
    #slug = models.SlugField(max_length=255, unique=True)  # add slug field
    # add more fields here if needed

    class Meta:
        """
        Metadata for the Post model.
        """
        ordering = ['-published_date']

    def __str__(self):
        """
        String representation of a post instance.
        """
        return self.title

    #def save(self, *args, **kwargs):
    #    """
    #    Custom save method to generate slug.
    #    """
    #    if not self.slug:
    #        self.slug = slugify(self.title)
    #    super().save(*args, **kwargs)

    # add more methods here if needed
