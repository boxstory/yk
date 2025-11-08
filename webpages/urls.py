from django.urls import path
from webpages import views as webpages_views
from accounts import views as accounts_views


app_name = 'webpages'



urlpatterns = [
     path('', webpages_views.home, name='home'),
     path('*/', webpages_views.home, name='home1'),


     # webpage urls ----------------------------------------------------------------
     path('about/', webpages_views.about, name='about'),
     path('contact/', webpages_views.contact, name='contact'),
     path('join_leads/', webpages_views.join_leads, name='join_leads'),
     path('services/', webpages_views.services, name='services'),
     path('property_services/', webpages_views.property_services, name='property_services'),
     path('property_services/join/', webpages_views.property_join, name='property_join'),
     path('workman_services/', webpages_views.workman_services, name='workman_services'),
     path('workman_services/join/', webpages_views.workman_join, name='workman_join'),
     path('realtor_services/', webpages_views.realtor_services, name='realtor_services'),
     path('realtor_services/join/', webpages_views.realtor_join, name='realtor_join'),
     path('careers/add/', webpages_views.careers_add, name='careers_add'),
     path('careers/', webpages_views.careers_list, name='careers_list'),
     path('careers_submit/<int:job_id>/', webpages_views.careers_submit, name='careers_submit'),
     
     path('dashboard/', webpages_views.choose_dashboard, name='choose_dashboard'),

     path('group_memebership/', webpages_views.group_memebership.as_view(),
          name='group_memebership'),
     path('whatsapp_group/', webpages_views.whatsapp_group,
          name='whatsapp_group'),

     # API endpoints ----------------------------------------------------------------
     path('api/docs/', webpages_views.api_documentation, name='api_documentation'),
     path('api/health/', webpages_views.api_health, name='api_health'),

]
