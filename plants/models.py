from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, 'Available'), (1, 'Taken'))


class Category(models.Model):
    category = models.CharField(max_length=80)


class Plant(models.Model):
    title = models.CharField(max_length=40)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plants')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)
    description = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    wants = models.CharField(max_length=140, null=True, blank=True)
    added_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-added_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    ad = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    added_on = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-added_on']

    def __str__(self):
        return f'{self.name} commented: {self.body}'


class Message(models.Model):
    ad = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='ad')
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='sender')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='receiver')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Message from {self.sender} about {self.ad}'

