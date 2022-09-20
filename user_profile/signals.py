import profile
from .models import UserProfile
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
User = get_user_model()


@receiver(post_delete, sender=UserProfile)
def deleteProfile(instance, **kwargs):
    instance.user.delete()



@receiver(post_save, sender=User)
def createProfile(instance, **kwargs):
    UserProfile.objects.create(user=instance)