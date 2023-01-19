from django.urls import path

from accounts import views as accounts_views

app_name = 'accounts'
urlpatterns = [

    path('agent/', accounts_views.agent_profile, name='agent_profile'),

]
