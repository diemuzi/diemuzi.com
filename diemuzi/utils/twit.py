import twitter
from django.conf import settings


class Twitter:
    def __init__(self):
        self.api = twitter.Api(consumer_key=settings.TWITTER_API_KEY,
                               consumer_secret=settings.TWITTER_API_SECRET,
                               access_token_key=settings.TWITTER_ACCESS_TOKEN,
                               access_token_secret=settings.TWITTER_ACCESS_SECRET)

    def post(self, message):
        return self.api.PostUpdate(status=message)
