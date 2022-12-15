from django.db import models
from datetime import datetime

# Create your models here.


class GroupList(models.Model):
    group_name = models.CharField(default="none", max_length=20)
    group_no = models.CharField(default=0, max_length=3)
    group_link = models.CharField(blank=True, null=True, max_length=100)
    group_platform = models.CharField(default='whatsapp', max_length=10)
    member_count = models.CharField(default=0, max_length=4)

    def __str__(self):
        return self.group_name


class MobSubscriber(models.Model):
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=8)
    is_owner = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    date_subscribed = models.DateTimeField(default=datetime.now)
    whatsapp_group_id = models.ManyToManyField(
        GroupList, blank=True)

    def __str__(self):
        return self.mobile_no

    class Meta:
        verbose_name = "Mobile Subscriber"
        verbose_name_plural = "Mobile Subscribers"

class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"
