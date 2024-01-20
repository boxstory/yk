from django.urls import path

from accounts import views as accounts_views

app_name = 'accounts'
urlpatterns = [
    # accounts urls ----------------------------------------------------------------
    path('profile/', accounts_views.user_profile, name='user_profile'),
    path('profile/<int:pk>/update/', accounts_views.update_user_profile, name='update_user_profile'),



    # accounts urls ----------------------------------------------------------------
    path('agent/', accounts_views.agent_profile, name='agent_profile'),
    path('join_marketing/', accounts_views.join_marketing, name='join_agent'),



    # accounts urls ----------------------------------------------------------------



]
