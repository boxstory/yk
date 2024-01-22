from django.db import models
from datetime import datetime, timedelta

# Create your models here.


class GroupList(models.Model):
    group_name = models.CharField(default="none", max_length=100)
    group_no = models.CharField(default=0, max_length=3)
    group_link = models.CharField(blank=True, null=True, max_length=100)
    group_platform = models.CharField(default='whatsapp', max_length=100)
    member_count = models.CharField(default=0, max_length=4)
    discription = models.CharField(default=0, max_length=100)

    def __str__(self):
        return self.group_name

def get_deadline():
    return datetime.today() + timedelta(days=20)


Category_choices = (
    ('management', 'Management Jobs'),
    ('accounting', 'Accounting Jobs'),
    ('medical', 'Medical Jobs'),
    ('services', 'Services Jobs'),
    ('technology', 'Technology Jobs'),
    ('maintenance', 'Maintenance Jobs'),
)
class JobList(models.Model):
    job_title = models.CharField(default="none", max_length=100)
    company = models.CharField(default="none", max_length=100)
    job_nature = models.CharField(default='Full Time', max_length=100)
    category = models.CharField(choices=Category_choices , max_length=100)
    job_no = models.CharField(default=0, max_length=4)
    job_location = models.CharField(default='Doha', max_length=4)
    payment_range = models.CharField(default=0, max_length=100)
    job_discription = models.CharField(default=0, max_length=200)
    job_tags = models.CharField(default='qatar', max_length=200)
    job_post_date = models.DateTimeField(default=datetime.now)
    job_deadline = models.DateField(default=get_deadline)

    def __str__(self):
        return self.job_title
    def get_tags_list(self):
        return self.job_tags.split(",") if self.job_tags else []

class MobSubscriber(models.Model):
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=8)
    is_clients = models.BooleanField(default=False)
    is_realator = models.BooleanField(default=False)
    is_workman = models.BooleanField(default=False)
    date_subscribed = models.DateTimeField(default=datetime.now)
    whatsapp_group_id = models.ManyToManyField(
        GroupList, blank=True)

    def __str__(self):
        return self.mobile_no

    class Meta:
        verbose_name = "Mobile Subscriber"
        verbose_name_plural = "Mobile Subscribers"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"


class CareersApplication(models.Model):
    full_name = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=255)
    visa_status = models.CharField(max_length=100)
    category = models.CharField(choices=Category_choices , max_length=100)
    job_id = models.CharField(max_length=255)
    email = models.EmailField()
    postion = models.CharField(max_length=255)
    self_intro = models.TextField(max_length=255)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Careers Application"
        verbose_name_plural = "Careers Applications"