# reservation/models.py

from django.db import models
from django.conf import settings
from performance.models import Performance

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('scheduled', '예약됨'),
        ('completed', '완료됨'),
        ('cancelled', '취소됨'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reservations')
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    reserved_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')

    def __str__(self):
        return f"{self.user} - {self.performance.artist} ({self.status})"