from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    name = models.CharField(max_length=50)
    customer_email = models.EmailField(max_length=100)
    customer_phone = models.IntegerField()
    party_size = models.IntegerField()
    date_time = models.DateTimeField()
    special_occasion = models.BooleanField(default=False)
    special_requirements = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking request from {self.name} for {self.party_size} people"
