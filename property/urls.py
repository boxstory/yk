from django.urls import path

from . import views

urlpatterns = [
    path('', views.propertyindex, name='propertyindex'),
    #path('<int:property_id>/', views.detail, name='detail'),
]
