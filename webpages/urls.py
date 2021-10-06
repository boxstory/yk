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



]
