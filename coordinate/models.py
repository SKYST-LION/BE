from django.db import models
from performance.models import Performance

class Coordinate(models.Model):
    performance = models.OneToOneField(
        Performance,
        on_delete=models.CASCADE,
        related_name='coordinate'
    )
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.performance.artist} - ({self.latitude}, {self.longitude})"