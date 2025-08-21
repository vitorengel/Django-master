from django.db.models.signals import pre_delete, pre_save, post_delete, post_save
from django.dispatch import receiver
from cars.models import Car


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    ...


@receiver(post_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    ...


@receiver(pre_delete, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    ...


@receiver(post_delete, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    ...