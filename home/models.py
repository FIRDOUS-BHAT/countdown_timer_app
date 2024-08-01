from django.db import models

# Create your models here.


class Event(models.Model):
    """
    A model to store the countdown timer data.
    """
    name = models.CharField(max_length=100)
    event_date = models.DateTimeField()

    def __str__(self):
        return self.name