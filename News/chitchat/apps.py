from django.apps import AppConfig


class ChitchatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chitchat'

    def ready(self):
        from . import signals  # выполнение модуля -> регистрация сигналов