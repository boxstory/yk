from django.urls import path

from clients import views as clients_views

app_name = 'clients'
# main path('property/', include('property.urls'), name='property'),

urlpatterns = [
    path('', clients_views.dashboard, name='dashboard'),
    
]