from django.conf import settings

from utils.twit import Twitter


def create_twitter_blog(sender, instance, created, **kwargs):
    if created:
        url = 'https://diemuzi.com/blog/' + instance.slug

        if settings.TWITTER_ACTIVE:
            Twitter().post(message='A new blog has been published - ' + url)
