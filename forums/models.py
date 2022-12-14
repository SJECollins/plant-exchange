from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Forum(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=280)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Discussion(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='discussions')
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=80)
    content = models.TextField()
    image = CloudinaryField('image', null=True, blank=True)
    created_on = models.DateField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    is_open = models.BooleanField(default=True)

    class Meta:
        ordering = ['is_open']
        get_latest_by = ['created_on']
    
    def __str__(self):
        return self.title

    
class Post(models.Model):
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='posts')
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    image = CloudinaryField('image', null=True, blank=True)
    deleted = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']
        get_latest_by = ['created_on']

    def __str__(self):
        return self.content
