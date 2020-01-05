from django.contrib import sitemaps
from django.urls import reverse

from blog import models


class StaticSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return [
            'blog:index',
            'blog:search'
        ]

    def location(self, item):
        return reverse(item)


class DynamicSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return models.Blog.objects.all().order_by('date_from')

    def location(self, item):
        return reverse('blog:read', kwargs={'slug': item.slug})


class DynamicSitemapCategory(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return models.Category.objects.all().order_by('name')

    def location(self, item):
        return reverse('blog:search', kwargs={'category': item.slug})
