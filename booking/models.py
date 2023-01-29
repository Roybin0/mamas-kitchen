from django.db import models
from django.contrib.auth.models import User


CONFIRMED = ((0, "Not confirmed"), (1, "Confirmed"))


class Booking(models.Model):
    name = models.CharField(max_length=50)
    customer_email = models.EmailField(max_length=100)
    customer_phone = models.IntegerField()
    party_size = models.IntegerField()
    date_time = models.DateTimeField()
    sp_occasion = models.BooleanField(default=False)
    sp_requirements = models.BooleanField(default=False)
    confirmed = models.IntegerField(CONFIRMED, default=0)

    def __str__(self):
        return f"Booking request from {self.name} for {self.party_size} people"
