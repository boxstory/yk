from django.urls import path

from clients import views as clients_views

app_name = 'clients'
# main path('property/', include('property.urls'), name='property'),

urlpatterns = [
    path('dashboard/', clients_views.dashboard, name='dashboard'),
    path('dashboard/property/own/', clients_views.property_all_list, name='property_all_list' ),
    path('dashboard/property/add/', clients_views.property_create, name='property_create'),
    path('dashboard/property/update/', clients_views.property_update, name='property_update'),
    
    
    path('dashboard/portions/', clients_views.portions_all_list, name='portions_all_list' ),
    path('dashboard/<int:property_id>/portions/', clients_views.portions_a_building, name='portions_a_building' ),
    path('dashboard/<int:property_id>/portions/add/', clients_views.portions_add, name='portions_add' ),
    path('dashboard/portions/<int:portions_id>/update/', clients_views.portions_update, name='portions_update' ),
    
]