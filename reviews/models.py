from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from booking.models import Booking


class Review(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    customer_name = models.ForeignKey(
        Booking, on_delete=models.PROTECT, related_name="cust_name")
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField
    image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"Review {self.content} left by {self.customer_name}"
