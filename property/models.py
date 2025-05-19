from django.conf import settings
from django.db import models
from django.utils.text import slugify
# Create your models here.


def portion_image_location(instance, filename):
    print('portion_image_location')
    print(instance.building_data.user.id,)
    print(instance.building_data.client_code)
    print(instance.unit_no)
    print(filename)
    return 'property/{0}/{1}/{2}/portion-{3}'.format(instance.building_data.user.id, instance.building_data.client_code, instance.unit_no, filename)


def property_image_location(instance, filename):
    print('property_image_location')
    print(instance.user.id)
    print(instance.client_code)
    print(filename)
    url = 'property/{0}/{1}/Building-{2}'.format(instance.user.id,
                                                 instance.client_code, filename)
    print(url)
    return url


class Building_data(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='building_data')
    title = models.CharField(max_length=100)
    client_code = models.CharField(
        max_length=100, help_text='Enter client side building code')
    building_code = models.CharField(
        max_length=100 )
    landmark = models.CharField(max_length=100)
    zone_no = models.IntegerField(default=0)
    street_no = models.IntegerField(default=0, blank=True)
    building_no = models.IntegerField(default=0, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    photo_main = models.ImageField(upload_to=property_image_location, default='property/building_default.png',
                                   help_text='Upload a Featured outside photo', blank=True)
    portion_count = models.IntegerField(default=0) 

    def __str__(self):
        return f'{self.zone_no}, {self.building_no}'


class Portions(models.Model):
    CHOICES = (
        ('Furnished', 'Furnished'),
        ('Semi-Furnished', 'Semi-Furnished'),
        ('UnFurnished', 'UnFurnished'),
    )
    PORTION_CHOICES = (
        ('BACHLOR_BEDSPACE', 'BACHLOR_BEDSPACE'),
        ('SINGLE_ROOM', 'SINGLE_ROOM'),
        ('STUDIO', 'STUDIO'),   
        ('1BHK', '1BHK'),
        ('2BHK', '2BHK'),
        ('3BHK', '3BHK'),
        ('4BHK', '4BHK'),
        ('5BHK', '5BHK'),
        ('5+BHK', '5+BHK'),
        ('VILLA', 'VILLA'),
        ('APARTMENT', 'APARTMENT'),
        ('CAMPSITE', 'CAMPSITE'),
        ('OFFICE', 'OFFICE'),
        ('SHOP', 'SHOP'),
        ('STORAGE', 'STORAGE'),
        ('OTHER', 'OTHER'),
    )
    building_data = models.ForeignKey(
        Building_data, on_delete=models.CASCADE, related_name='portions')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='portions')
    portion_code = models.CharField(
        max_length=100, default='10001')
    unit_no = models.IntegerField(default=0, blank=True)
    floor_no = models.IntegerField(default=0, blank=True)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField(default=1)
    bathrooms = models.IntegerField(default=1)
    portion_type = models.CharField(
        max_length=100, choices=PORTION_CHOICES, default='STUDIO')
    furnished_type = models.CharField(
        max_length=100, choices=CHOICES, default='No')
    furnished_extra_info = models.CharField(
        max_length=100, blank=True, help_text='Enter Furnished items lists',)
    sqft = models.IntegerField(default=0, blank=True)
    photo_main = models.ImageField(upload_to=portion_image_location,
                                   help_text='Upload a Featured photo', blank=True)
    photo_1 = models.ImageField(
        upload_to=property_image_location, blank=True)
    photo_2 = models.ImageField(
        upload_to=property_image_location, blank=True)
    photo_3 = models.ImageField(
        upload_to=property_image_location, blank=True)

    # slug = AutoSlugField(populate_from='title')

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Unit No: {self.unit_no}, Code: {self.portion_code}'

    meta = {
        'indexes': ['-date_created', '-date_updated'],
        'ordering': ['-date_created', '-date_updated']
    }

    class Meta:
        verbose_name = "Portion"
        verbose_name_plural = "Portions"


class Portions_status(models.Model):
    CHOICES = (
        ('OCCUPIED', 'Occupied'),
        ('VACANT', 'Vacant'),
        ('BOOKED', 'Booked'),
        ('VACANT_SOON', 'Vacant soon'),
        ('CLOSED', 'Closed'),
        ('NOT_SET', 'Not Set'),
    )
    portions = models.ForeignKey(
        Portions, on_delete=models.CASCADE, related_name='portions_status')
    vacant_date = models.DateField(help_text='Enter date upcoming vacant')
    status = models.CharField(
        max_length=100, choices=CHOICES, default='Occupied')

    def __str__(self):
        return f'Portion id: {self.portions_id}, Status: {self.status}'

    meta = {
        'indexes': ['-status'],
        'ordering': ['-vacant_date']
    }


class Zone_names(models.Model):
    zone_name = models.CharField(max_length=100)
    zone_no = models.IntegerField(default=0)

    def __str__(self):
        return self.zone_name
    meta = {
        'indexes': ['-zone_no'],
        'ordering': ['-zone_no']
    }

    class Meta:
        verbose_name = "Zone Name"
        verbose_name_plural = "Zone Names"


class Inquire(models.Model):
    CHOICES = (
        ('Any', 'Any'),
        ('Furnished', 'Furnished'),
        ('Semi-Furnished', 'Semi-Furnished'),
        ('UnFurnished', 'UnFurnished'),
    )
    PORTIONS_CHOICES = (
        ('1BHK', '1BHK'),
        ('2BHK', '2BHK'),
        ('3BHK', '3BHK'),
        ('OFFICE', 'OFFICE'),
        ('SHOP', 'SHOP'),
        ('STORAGE', 'STORAGE'),
        ('OTHER', 'OTHER'),
    )

    name = models.CharField(max_length=100)
    mobile_no = models.IntegerField(default=0)
    whatsapp_no = models.IntegerField(default=0)
    locations = models.CharField(max_length=100, blank=True)
    date_from = models.DateTimeField()
    duration = models.IntegerField()
    price_from = models.IntegerField()
    price_to = models.IntegerField()
    furnished_type = models.CharField(
        max_length=100, choices=CHOICES, default='Any')
    property_type = models.CharField(
        max_length=100, choices=PORTIONS_CHOICES, blank=True, help_text='Choose option from lists',)
    property_type_other = models.CharField(
        max_length=100, blank=True, help_text='Enter Other Lists',)

    notes = models.TextField(
        max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.mobile_no)
    meta = {
        'indexes': ['-mobile_no', 'date_from'],
        'ordering': ['-mobile_no', 'property_type', 'date_from']
    }
