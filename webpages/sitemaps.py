from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from webpages import models as webpage_models


class StaticViewSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return [  'webpages:home', 'webpages:services', 'webpages:about', 'webpages:contact']

    def location(self, item):
        return reverse(item)


class DynamicViewSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return webpage_models.Tags.objects.all()

    def location(self, item):
        return