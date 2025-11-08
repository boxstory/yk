from django.urls import path

from clients import views as clients_views

app_name = 'clients'
# main path('property/', include('property.urls'), name='property'),

urlpatterns = [
    path('dashboard/', clients_views.dashboard, name='dashboard'),
    path('dashboard/property/all/', clients_views.property_all_list, name='property_all_list' ),
    path('dashboard/property/own/', clients_views.property_own_list, name='property_own_list' ),
    path('dashboard/property/add/', clients_views.property_create, name='property_create'),
    path('dashboard/property/update/<int:property_id>/', clients_views.property_update, name='property_update'),


    path('dashboard/portions/', clients_views.portions_all_list, name='portions_all_list' ),
    path('dashboard/portions/vacant-soon/', clients_views.portions_vacant_soon, name='portions_vacant_soon'),
    path('dashboard/portions/vacants/', clients_views.portions_vacants, name='portions_vacants'),
    path('dashboard/portions/occupied/', clients_views.portions_occupied, name='portions_occupied'),
    path('dashboard/portions/unlisted/', clients_views.portions_unlisted, name='portions_unlisted'),
    path('dashboard/<int:property_id>/portions/', clients_views.portions_a_building, name='portions_a_building' ),
    path('dashboard/<int:property_id>/portions/add/', clients_views.portions_add, name='portions_add' ),
    path('dashboard/portions/<int:portions_id>/update/', clients_views.portions_update, name='portions_update' ),

]