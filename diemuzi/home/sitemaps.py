from django.contrib import sitemaps
from django.urls import reverse


class StaticSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return [
            'home:faq',
            'home:index',
            'home:privacy'
        ]

    def location(self, item):
        return reverse(item)
