
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from webpages.sitemaps import StaticViewSitemap
from django.views.generic import TemplateView


sitemaps = {
    'sitemap.xml': StaticViewSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls'), name='accounts'),
    path('', include('accounts.urls'), name='accounts'),
    path('', include(('webpages.urls', 'webpages'), namespace="webpages")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="webpages/robots.txt", content_type='text/plain')),
     
    path('property/', include('property.urls'), name='property'),
    path('realtor/', include('realtor.urls'), name='realtor'),
    path('clients/', include('clients.urls'), name='clients'),
    path('workman/', include('workman.urls'), name='workman'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'webpages.views.handler404'
handler500 = 'webpages.views.handler500'