from django.db import models
from django.conf import settings

# Create your models here.


class Roles(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    role = models.IntegerField(default=0)
    discripion = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name


def profile_image_location(instance, filename):
    print(instance)
    print(filename)
    print(instance.user.username)
    return 'agents/{0}/{1}'.format(instance.user.username, filename)


class Spoken_Languages(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Agent(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    roles = models.ForeignKey(
        Roles, on_delete=models.SET_NULL, null=True, default="1")
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=100)
    languages = models.ManyToManyField(
        Spoken_Languages, verbose_name="Languages", help_text="Select languages spoken")

    profile_image = models.ImageField(
        upload_to=profile_image_location, blank=True, null=True)
    NO = 'NO'
    YES = 'YES'
    APPROVAL = ((NO, 'no'), (YES, 'yes'))
    active = models.CharField(choices=APPROVAL, default=NO, max_length=3)
    verified = models.CharField(choices=APPROVAL, default=NO, max_length=3)

    def __str__(self):
        return self.name
