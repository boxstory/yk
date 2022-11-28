
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls'), name='accounts'),
    path('<int:pk>/dashboard/', include('accounts.urls')),
    path('', include(('webpages.urls', 'webpages'), namespace="webpages")),
    path('property/', include('property.urls'), name='property'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
