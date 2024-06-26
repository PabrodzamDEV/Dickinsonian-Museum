from django.apps import AppConfig


class MuseumConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Museum'

    def ready(self):
        import Museum.signals
