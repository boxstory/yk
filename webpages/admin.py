from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(MobSubscriber)
class MobSubscriberAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile_no')

    class Meta:
        model = MobSubscriber


admin.site.register(GroupList)


admin.site.register(Contact)
