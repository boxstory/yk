from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(MobSubscriber)
class MobSubscriberAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile_no')

    class Meta:
        model = MobSubscriber


admin.site.register(GroupList)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')

    class Meta:
        model = Contact


@admin.register(JobList)
class JobListAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'job_nature', 'job_post_date')

    class Meta:
        model = JobList

@admin.register(CareersApplication)
class CareersApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'postion', 'contact_no')

    class Meta:
        model = CareersApplication