from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Review(models.Model):
    title = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    reply = models.TextField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"Review {self.content} left by {self.customer_name}"
