from django.apps import AppConfig

class BlogConfig(AppConfig):
    """
    Configuration class for the Blog app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        """
        Override the ready method to perform initialization tasks when the app is ready.
        """
        pass  # Add any initialization tasks here if needed
