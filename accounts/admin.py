from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Profile)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email')

    class Meta:
        model = Profile

@admin.register(ProfilePicture)
class ProfilesPictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'profile', 'profile_picture',)

    class Meta:
        model = ProfilePicture

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