from django.db import models
from datetime import datetime

# Create your models here.


class MobSubscriber(models.Model):
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=12)
    date_subscribed = models.DateTimeField(default=datetime.now)
    messages_received = models.IntegerField(default=0)

    def __str__(self):
        return self.name, self.mobile_no
