from django.apps import AppConfig
import logging

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        """
        Override the ready method to import signals when the application is ready.
        This ensures that signal handlers are connected when the application starts.
        """
        try:
            import users.signals
        except ImportError as e:
            logging.error(f"Error importing users.signals: {e}")
