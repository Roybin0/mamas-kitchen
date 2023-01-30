from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField


class Booking(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    party_size = models.PositiveSmallIntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
    date_time = models.DateTimeField()
    special_occasion = models.BooleanField(default=False)
    special_requirements = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking request from {self.name} for {self.party_size} people"


class Review(models.Model):
    title = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    reply = models.TextField()
    likes = models.ManyToManyField(
        User, related_name='review_like', blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"Review {self.title} left by {self.customer_name}"
