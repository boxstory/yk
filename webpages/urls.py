from django.urls import path
from . import views
from . import contact

app_name = 'webpages'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('profile/', views.profile, name='profile'),
    path('add_property/', views.add_property, name='add_property'),
    path('join_marketing/',views.join_marketing, name='join_marketing'),


]
