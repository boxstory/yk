
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls'), name='accounts'),
    path('', include('accounts.urls'), name='accounts'),
    path('', include(('webpages.urls', 'webpages'), namespace="webpages")),
    path('property/', include('property.urls'), name='property'),
    path('realtor/', include('realtor.urls'), name='realtor'),
    path('clients/', include('clients.urls'), name='clients'),
    path('workman/', include('workman.urls'), name='workman'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'webpages.views.handler404'
handler500 = 'webpages.views.handler500'