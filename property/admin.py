from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Building_info)
class BuildingInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'landmark', 'zone_no', 'street_no',
                    'building_no', 'date_created', 'date_updated')
    list_filter = ('landmark', 'zone_no', 'street_no',
                   'date_created', 'date_updated')
    search_fields = ('title', 'landmark', 'zone_no',
                     'street_no', 'building_no')
    list_per_page = 10

    class Meta:
        model = Building_info
        verbose_name = 'building'
        verbose_name_plural = 'buildings'


# admin.site.register(BuildingInfoAdmin)


@admin.register(Portions)
class PortionsAdmin(admin.ModelAdmin):
    list_display = ('unit_no', 'description', 'price', 'bedrooms', 'bathrooms',
                    'furnished_type', 'furnished_extra_info', 'sqft', 'photo_main', 'date_created', 'date_updated')
    list_filter = ('price', 'bedrooms', 'bathrooms',
                   'furnished_type', 'date_created', 'date_updated')
    search_fields = ('unit_no', 'description', 'price', 'bedrooms', 'bathrooms',
                     'furnished_type', 'furnished_extra_info', 'sqft', 'date_created', 'date_updated')
    list_per_page = 10

    class Meta:
        model = Portions
        verbose_name = 'portion'
        verbose_name_plural = 'portions'


# admin.site.register(PortionsAdmin)


@admin.register(Zone_names)
class Zone_namesAdmin(admin.ModelAdmin):
    list_display = ('zone_name', 'zone_no')
    list_filter = ('zone_name', 'zone_no')
    search_fields = ('zone_name', 'zone_no')
    list_per_page = 10

    class Meta:
        model = Zone_names
        verbose_name = 'Zone name'
        verbose_name_plural = 'Zone names'
