from django.db import models
from django.conf import settings
from django.forms import ValidationError


GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

# Profile models here.

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=255, blank=True, null=True, unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    whatsapp = models.CharField(max_length=15, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    nationlity = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    is_business = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_realtor = models.BooleanField(default=False)
    is_workman = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name_plural = "Profiles"
        
        
def user_directory_path(instance, filename):
   return '%s/%s' % (instance.username, filename)


class ProfilePicture(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile_picture')
    profile = models.ForeignKey(Profile,  on_delete=models.CASCADE, related_name='profile_picture')
    profile_picture = models.ImageField(
        upload_to=user_directory_path , default='accounts/defaults/avatar.png', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
    
class Roles(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    role = models.IntegerField(default=0)
    discripion = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"


def agent_image_location(instance, filename):
    print(instance)
    print(filename)
    print(instance.user.username)
    return 'agents/{0}/{1}'.format(instance.user.username, filename)


class Spoken_Languages(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Spoken Language"
        verbose_name_plural = "Spoken Languages"


class Agent(models.Model):
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='agent')
    agent_name = models.CharField(max_length=255, blank=True, null=True)
    marketing_name = models.CharField(max_length=255, blank=True, null=True)
    roles = models.ForeignKey(
        Roles, on_delete=models.SET_NULL, null=True, default="1")
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=100)
    languages = models.ManyToManyField(
        Spoken_Languages, verbose_name="Languages", help_text="Select languages spoken")

    profile_image = models.ImageField(
        upload_to=agent_image_location, blank=True, null=True)
    NO = 'NO'
    YES = 'YES'
    APPROVAL = (
        ('NO', 'no'),
        ('YES', 'yes'),
    )
    active = models.CharField(choices=APPROVAL, default=NO, max_length=3)
    verified = models.CharField(choices=APPROVAL, default=NO, max_length=3)

    def __str__(self):
        return self.name
