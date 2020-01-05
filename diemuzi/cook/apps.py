from django.apps import AppConfig
from django.db.models.signals import post_save


class CookConfig(AppConfig):
    name = 'cook'

    def ready(self):
        from cook import models
        from cook import signals

        post_save.connect(signals.create_twitter_cook, sender=models.Cook)
