from django.conf import settings

from utils.twit import Twitter


def create_twitter_cook(sender, instance, created, **kwargs):
    if created:
        url = 'https://local.diemuzi.com:8443/cook/' + instance.slug

        if settings.TWITTER_ACTIVE:
            Twitter().post(message='A new cooking recipe has been published - ' + url)
