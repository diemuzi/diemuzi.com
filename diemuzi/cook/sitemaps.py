from django.contrib import sitemaps
from django.urls import reverse

from cook import models


class StaticSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return [
            'cook:index',
            'cook:search'
        ]

    def location(self, item):
        return reverse(item)


class DynamicSitemapRead(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return models.Cook.objects.all().order_by('date_from')

    def location(self, item):
        return reverse('cook:read', kwargs={'slug': item.slug})


class DynamicSitemapCategory(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return models.Category.objects.all().order_by('name')

    def location(self, item):
        return reverse('cook:search', kwargs={'category': item.slug})
