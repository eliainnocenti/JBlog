from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
import logging

logger = logging.getLogger(__name__)

# Create a user profile when a new user is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Signal to create a Profile object whenever a new User is created.
    """
    if created:
        try:
            Profile.objects.create(user=instance)
            logger.info(f'Profile created for user {instance.username}')
        except Exception as e:
            logger.error(f'Error creating profile for user {instance.username}: {e}')

# Save the user profile when the user is saved
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Signal to save the Profile object whenever the User is saved.
    """
    try:
        instance.profile.save()
        logger.info(f'Profile saved for user {instance.username}')
    except Profile.DoesNotExist:
        # This should not happen because the profile should be created on user creation
        logger.warning(f'Profile does not exist for user {instance.username}, creating profile...')
        Profile.objects.create(user=instance)
    except Exception as e:
        logger.error(f'Error saving profile for user {instance.username}: {e}')
