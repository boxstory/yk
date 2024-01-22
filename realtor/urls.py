from django.urls import path

from realtor import views as realtor_views

app_name = 'realtor'

urlpatterns = [
    path('', realtor_views.dashboard, name='dashboard'),
    
]