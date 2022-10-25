from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True, blank=True)
    location = models.CharField(max_length=40, null=True, blank=True, default='Private')
    about_me = models.CharField(max_length=140, null=True, blank=True)
    interested_in = models.CharField(max_length=140, null=True, blank=True)

    def __str__(self):
        return f"{self.name}'s Profile" 
