from django.urls import path
from webpages import views
from accounts import views as accounts_views

app_name = 'webpages'

urlpatterns = [
    path('', views.home, name='home'),
    path('join_marketing', accounts_views.join_marketing, name='join_agent'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('profile/', views.profile, name='profile'),


    path('group_memebership/', views.group_memebership.as_view(),
         name='group_memebership'),

    path('whatsapp_group/', views.whatsapp_group,
         name='whatsapp_group'),

]
