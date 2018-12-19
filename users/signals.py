# *args and **kwargs are mostly used in function definitions.
# *args and **kwargs allow you to pass a variable number of arguments to a function.
# What variable means here is that you do not know beforehand how many arguments can be passed to your function
# by the user so in this case you use these two keywords.

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User) #post_save is signal
def create_profile(sender, instance, created, **kwargs): #receiver is create_profile function
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User) #post_save is signal
def save_profile(sender, instance, **kwargs): #kwargs olayına bak
    instance.profile.save()
