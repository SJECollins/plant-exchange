from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True, blank=True)
    location = models.CharField(max_length=40, null=True, blank=True, default='Private')
    about_me = models.CharField(max_length=140, null=True, blank=True)
    interested_in = models.CharField(max_length=140, null=True, blank=True)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Profile" 

    def get_absolute_url(self):
        return reverse('profiles:profile', kwargs={'user_id': self.user.id})


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)