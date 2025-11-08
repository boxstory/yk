from django.urls import path
from .views import help_view, workman_help, realtor_help, client_help

app_name = 'help'
urlpatterns = [
    path('', help_view, name='help'),
    path('workman/', workman_help, name='workman_help'),
    path('realtor/', realtor_help, name='realtor_help'),
    path('client/', client_help, name='client_help'),
]
