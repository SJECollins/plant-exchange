from django.db import models
from django.contrib.auth.models import User


class Forum(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=280)

    class Meta:
        ordering = ['title']

    def __str__:
        return self.title


class Discussion(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='discussions')
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=280)
    created_on = models.DateField(auto_now_add=True)
    is_open = models.BooleanField(default=True)

    class Meta:
        ordering = ['is_open']
    
    def __str__:
        return self.title

    
class Post(models.Model):
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='posts')
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__:
        return self.content
