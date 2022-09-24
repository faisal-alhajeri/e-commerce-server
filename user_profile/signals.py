from .models import UserProfile
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from cart.models import Cart

User = get_user_model()


@receiver(post_delete, sender=UserProfile)
def deleteProfile(instance, **kwargs):
    instance.user.delete()



@receiver(post_save, sender=User)
def createProfile(instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_delete, sender=Cart)
def cartCreate(instance, **kwargs):
    instance.profile.delete()



@receiver(post_save, sender=UserProfile)
def createCart(instance,  created, **kwargs):
    if created:
        Cart.objects.create(profile=instance)