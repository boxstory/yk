from django.urls import path

from workman import views as workman_views

app_name = 'workman'
# main path('property/', include('property.urls'), name='property'),

urlpatterns = [
    path('', workman_views.dashboard, name='dashboard'),
    
]