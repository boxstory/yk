
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Portions





@receiver(post_save, sender=Portions)
def update_portion_count_on_save(sender, instance, created, **kwargs):
    print('update_portion_count_on_save')
    print(instance)
    print(created)
    if created:
        instance.property_data.portion_count += 1
        instance.property_data.save()


@receiver(post_delete, sender=Portions)
def update_portion_count_on_delete(sender, instance, **kwargs):
    print('update_portion_count_on_delete   ')
    print(instance)
    instance.property_data.portion_count -= 1
    instance.property_data.save()