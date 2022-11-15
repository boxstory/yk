from django.urls import path

from property import views

app_name = 'property'
# main path('property/', include('property.urls'), name='property'),

urlpatterns = [
    path('', views.property_all, name='property_all'),

    # buildings
    path('<int:pk>/', views.own_building, name='own_building'),
    path('<int:pk>/add/', views.building_create, name='building_create'),
    path('<int:pk>/<int:building_id>/update/',
         views.building_update, name='building_update'),

    # portions
    path('<int:pk>/<int:building_id>/',
         views.portion_all, name='portion_all'),
    path('<int:pk>/<int:building_id>/add/',
         views.portion_add, name='portion_add'),
    path('<int:pk>/<int:building_id>/<int:portion_id>/',
         views.portion_single, name='portion_single'),
    path('<int:pk>/<int:building_id>/<int:portion_id>/update',
         views.portion_update, name='portion_update'),

]
