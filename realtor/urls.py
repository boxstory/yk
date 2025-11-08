from django.urls import path

from realtor import views as realtor_views

app_name = 'realtor'

urlpatterns = [
    path('', realtor_views.dashboard, name='dashboard'),
    path('near-properties/', realtor_views.near_properties, name='realtor_near_properties'),
    path('vacant-portions/', realtor_views.vacant_portions, name='realtor_vacant_portions'),
    path('vacant-soon/', realtor_views.vacant_soon, name='realtor_vacant_soon'),
    path('vacants/', realtor_views.vacants, name='realtor_vacants'),
    path('booked-properties/', realtor_views.booked_properties, name='realtor_booked_properties'),
    path('inquiries/', realtor_views.inquiries, name='realtor_inquiries'),
    path('tenant-calls/', realtor_views.tenant_calls, name='realtor_tenant_calls'),
    path('visit-requests/', realtor_views.visit_requests, name='realtor_visit_requests'),
    path('followups/', realtor_views.followups, name='realtor_followups'),
    path('tenant-docs/', realtor_views.tenant_docs, name='realtor_tenant_docs'),
    path('deals-reports/', realtor_views.deals_reports, name='realtor_deals_reports'),
    path('pending-requests/', realtor_views.pending_requests, name='realtor_pending_requests'),
    path('reports/', realtor_views.reports, name='realtor_reports'),
    path('contacts/', realtor_views.contacts, name='realtor_contacts'),
    path('services-list/', realtor_views.services_list, name='realtor_services_list'),
]