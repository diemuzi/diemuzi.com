from django.apps import AppConfig
from django.db.models.signals import post_save


class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self):
        from blog import models
        from blog import signals

        post_save.connect(signals.create_twitter_blog, sender=models.Blog)
