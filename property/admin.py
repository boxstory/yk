from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'landmark', 'zone_no', 'street_no', 'building_no', 'unit_no', 'description', 'price', 'bedrooms', 'bathrooms',
                    'furnished', 'furnished_extra_info', 'sqft', 'photo_main', 'photo_1', 'photo_2', 'photo_3', 'date_created', 'date_updated')
    list_filter = ('zone_no', 'street_no',  'price', 'bedrooms', 'bathrooms',
                   'furnished', 'date_created', 'date_updated')
    search_fields = ('title', 'landmark', 'zone_no', 'street_no', 'building_no', 'unit_no', 'description', 'price', 'bedrooms', 'bathrooms',
                     'furnished', 'furnished_extra_info', 'sqft', 'photo_main', 'photo_1', 'photo_2', 'photo_3', 'date_created', 'date_updated')
    list_per_page = 10

    class Meta:
        model = Property
        verbose_name = 'property'
        verbose_name_plural = 'properties'


admin.site.register(Property_info)


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
