from django.urls import path

from property import views

app_name = 'property'
# main path('property/', include('property.urls'), name='property'),

urlpatterns = [
    # inquire display add
    path('inquire/lists/', views.inquire_lists, name='inquire_lists'),
    path('inquire/add/', views.inquire_create, name='inquire_create'),

    # buildings display
    path('', views.building_all, name='building_all'),
    # buildings add update delete
    path('<int:pk>/add/', views.building_create, name='building_create'),
    path('<int:pk>/single_add/', views.building_plus_portion_create, name='building_plus_portion_create'),
    path('<int:pk>/<int:building_id>/update/',
         views.building_update, name='building_update'),

     # portions list for realtor
    path('<int:pk>/portions_list_all/',
         views.portions_list_all, name='portions_list_all'),
    path('<int:pk>/<int:building_id>/<int:portion_id>/details/',
         views.portion_single_details, name='portion_single_details'),
    path('<int:pk>/<int:building_id>/all/',
         views.portions_of_building, name='portions_of_building'),
    
    # own bbuildings & own portions display
    path('<int:pk>/', views.building_own, name='building_own'),
    path('<int:pk>/portions_own_buildings/',
         views.portions_own_buildings, name='portions_own_buildings'),


     # portion add update delete
    path('<int:pk>/<int:building_id>/add/',
         views.portion_single_add, name='portion_single_add'),
    path('<int:pk>/<int:building_id>/<int:portion_id>/update',
         views.portion_single_update, name='portion_single_update'),

     #  portion status list display / portion status update
    path('<int:portion_id>/vacant_status_update',
         views.vacant_status_update, name='vacant_status_update'),
    path('<int:pk>/<int:building_id>/portion_status_list',
         views.portion_status_list, name='portion_status_list'),

]
