from django.urls import path

from accounts import views as accounts_views

app_name = 'accounts'

urlpatterns = [
    # accounts urls ----------------------------------------------------------------
    path('profile/', accounts_views.profile, name='profile'),
    path('profile/update/', accounts_views.profile_update, name='profile_update'),
    path('profile/picture/update/', accounts_views.profile_picture_update, name='profile_picture_update'),



    # accounts urls ----------------------------------------------------------------
    path('agent/', accounts_views.agent_profile, name='agent_profile'),
    path('join_marketing/', accounts_views.join_marketing, name='join_agent'),



    # accounts urls ----------------------------------------------------------------



]
