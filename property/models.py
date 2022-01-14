from django.conf import settings
from django.db import models
from django.utils.text import slugify
# Create your models here.


def property_image_location(instance, filename):
    return 'property/{0}/{1}/{2}'.format(instance.user.id, instance.property.id, filename)


class Property(models.Model):
    CHOICES = (
        ('Semi-Furnished', 'Semi-Furnished'),
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    zone_no = models.IntegerField(default=0)
    street_no = models.IntegerField(default=0, blank=True)
    building_no = models.IntegerField(default=0, blank=True)
    unit_no = models.IntegerField(default=0, blank=True)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    furnished = models.CharField(max_length=100, choices=CHOICES, default='No')
    furnished_extra_info = models.CharField(max_length=100, blank=True)
    sqft = models.IntegerField(default=0, blank=True)
    photo_main = models.ImageField(upload_to=property_image_location,
                                   help_text='Upload a Main photo for the Property', blank=True)
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
        return self.title

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.property_title)
    #     super(Property, self).save(*args, **kwargs)


class Property_info(models.Model):
    CHOICES = (
        ('OCCUPIED', 'Ocuppied'),
        ('VACANT', 'Vacant'),
        ('BOOKED', 'Booked'),
        ('VACANT_SOON', 'Vacant soon'),
    )
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    property_type = models.TextField()
    status = models.CharField(
        max_length=100, choices=CHOICES, default='Ocuppied')

    def __str__(self):
        return self.property_type

    def __unicode__(self):
        return


class Zone_names(models.Model):
    zone_name = models.CharField(max_length=100)
    zone_no = models.IntegerField(default=0)

    def __str__(self):
        return self.zone_name
