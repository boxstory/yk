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
    path('<int:pk>/', views.building_own, name='building_own'),
    # buildings add update delete
    path('<int:pk>/add/', views.building_create, name='building_create'),
    path('<int:pk>/single_add/', views.building_plus_portion_create, name='building_plus_portion_create'),
    path('<int:pk>/<int:building_id>/update/',
         views.building_update, name='building_update'),

    # portions display
    path('<int:pk>/portion_all_building/',
         views.portion_all_building, name='portion_all_building'),
    path('<int:pk>/<int:building_id>/<int:portion_id>/',
         views.portion_single, name='portion_single'),
    path('<int:pk>/<int:building_id>/',
         views.portion_single_building, name='portion_single_building'),

     # portion add update delete
    path('<int:pk>/<int:building_id>/add/',
         views.portion_add, name='portion_add'),
    path('<int:pk>/<int:building_id>/<int:portion_id>/update',
         views.portion_update, name='portion_update'),

     # vacant status display update
    path('<int:pk>/<int:building_id>/<int:portion_id>/vacant_status',
         views.vacant_status, name='vacant_status'),
    path('<int:pk>/<int:building_id>/portion_vacant_status_list_update',
         views.portion_vacant_status_list_update, name='portion_vacant_status_list_update'),

]
