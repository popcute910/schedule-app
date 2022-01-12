from django.conf import settings
from django.db import models
from django.utils import timezone

class Reservation(models.Model):
    date = models.DateField(default=timezone.now)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title