from django.urls import path

from property import views

app_name = 'property'
# main path('property/', include('property.urls'), name='property'),

urlpatterns = [
    path('', views.propertyindex, name='propertyindex'),
    path('add/', views.property_create, name='property_create'),
    path('<int:pk>/', views.own_properties, name='own_properties'),
    path('<int:pk>/add/', views.property_create, name='property_create'),
    path('<int:pk>/update/', views.property_update, name='property_update'),
    path('<int:pk>/<property_id>/', views.single_property, name='single_property'),

]
