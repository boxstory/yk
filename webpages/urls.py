from django.urls import path
from webpages import views as webpages_views
from accounts import views as accounts_views

app_name = 'webpages'

urlpatterns = [
    path('', webpages_views.home, name='home'),

    

    # webpage urls ----------------------------------------------------------------
    path('about/', webpages_views.about, name='about'),
    path('contact/', webpages_views.contact, name='contact'),
    path('services/', webpages_views.services, name='services'),
    path('careers/', webpages_views.careers_list, name='careers_list'),
    path('careers_submit/<int:job_id>/', webpages_views.careers_submit, name='careers_submit'),
    


    path('group_memebership/', webpages_views.group_memebership.as_view(),
         name='group_memebership'),
    path('whatsapp_group/', webpages_views.whatsapp_group,
         name='whatsapp_group'),

]
