from django.conf import settings
from django.contrib.sites.models import Site

from utils.twit import Twitter


def create_twitter_blog(sender, instance, created, **kwargs):
    if created:
        url = 'https://' + Site.objects.get_current().domain + '/blog/' + instance.slug

        if settings.TWITTER_ACTIVE:
            Twitter().post(message='A new blog has been published - ' + url)
