from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from webpages.models import JobList
from property.models import Portions


class StaticViewSitemap(Sitemap):
    """Sitemap for static pages."""
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        # Returns a list of URL names for static pages
        return [
            'webpages:home',
            'webpages:about',
            'webpages:services',
            'webpages:contact',
            'webpages:property_services',
            'webpages:realtor_services',
            'webpages:workman_services',
            'webpages:careers_list',
        ]

    def location(self, item):
        return reverse(item)


class JobListSitemap(Sitemap):
    """Sitemap for job listings."""
    changefreq = "daily"
    priority = 0.7

    def items(self):
        # Assuming JobList has a field to filter for active jobs
        return JobList.objects.all()


class PortionSitemap(Sitemap):
    """Sitemap for job listings."""
    changefreq = "daily"
    priority = 0.7

    def items(self):
        # Assuming JobList has a field to filter for active jobs
        return Portions.objects.all()
    


