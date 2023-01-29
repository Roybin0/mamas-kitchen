from django.db import models
from cloudinary.models import CloudinaryField


class MainsMenu(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class DessertMenu(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
