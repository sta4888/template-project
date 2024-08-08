from django.apps import AppConfig


class UseriConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'useri'

    def ready(self):
        import useri.signals
