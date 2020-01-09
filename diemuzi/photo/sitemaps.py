from django.contrib import sitemaps
from django.urls import reverse

from photo import models


class StaticSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return [
            'photo:index',
            'photo:search'
        ]

    def location(self, item):
        return reverse(item)


class DynamicSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return models.Photo.objects.all().order_by('date_from')

    def location(self, item):
        return reverse('photo:search', kwargs={'name': item.name})


class DynamicSitemapAlbum(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return models.Album.objects.all().order_by('name')

    def location(self, item):
        return reverse('photo:search', kwargs={'album': item.slug})
