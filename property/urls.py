from django.urls import path

from property import views

app_name = 'property'
# main path('property/', include('property.urls'), name='property'),

urlpatterns = [
    # inquire display add
    path('inquire/lists/', views.inquire_lists, name='inquire_lists'),
    path('inquire/add/', views.inquire_create, name='inquire_create'),

    # properties display
    path('', views.property_all, name='property_all'),
    # properties add update delete
    
    path('<int:pk>/single_add/', views.property_plus_portion_create, name='property_plus_portion_create'),


     # portions list for realtor
    path('<int:pk>/portions_list_all/',
         views.portions_list_all, name='portions_list_all'),
    path('<int:pk>/<int:property_id>/<int:portion_id>/details/',
         views.portion_single_details, name='portion_single_details'),
    path('<int:pk>/<int:property_id>/all/',
         views.portions_of_property, name='portions_of_property'),
    
    # own bproperties & own portions display
    path('<int:pk>/', views.property_own, name='property_own'),
    path('<int:pk>/portions_own_properties/',
         views.portions_own_properties, name='portions_own_properties'),

 
     

     #  portion status list display / portion status update
    path('<int:portion_id>/vacant_status_update',
         views.vacant_status_update, name='vacant_status_update'),
    path('<int:pk>/<int:property_id>/portion_status_list',
         views.portion_status_list, name='portion_status_list'),

]
