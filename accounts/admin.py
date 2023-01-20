from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roles', 'active')

    class Meta:
        model = Agent


@admin.register(Spoken_Languages)
class Spoken_LanguagesAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'name')

    class Meta:
        model = Spoken_Languages


@admin.register(Roles)
class RolesAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')

    class Meta:
        model = Roles


