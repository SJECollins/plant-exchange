from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, 'Available'), (1, 'Taken'))


class Category(models.Model):
    name = models.CharField(max_length=80)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Plant(models.Model):
    title = models.CharField(max_length=40)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default='none')
    description = models.TextField()
    image = CloudinaryField('image', null=True, blank=True, default='placeholder')
    will_trade_for = models.CharField(max_length=140, null=True, blank=True)
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
