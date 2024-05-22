from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os


class Profile(models.Model):
    """
    Profile model to store additional information for each user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # add more fields here if needed

    def __str__(self):
        """
        Return a string representation of the Profile object.
        """
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        """
        Override the save method to resize the image if necessary.
        """
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)

            # Ensure the directory exists before saving the image
            if not os.path.exists(os.path.dirname(self.image.path)):
                os.makedirs(os.path.dirname(self.image.path))

            img.save(self.image.path)
