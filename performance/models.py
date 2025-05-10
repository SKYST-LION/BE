from django.db import models
from django.conf import settings

class Performance(models.Model):
    artist = models.CharField(max_length=100)
    account = models.FloatField(null=True, blank=True)
    price = models.PositiveIntegerField()
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    latitude = models.FloatField(null=True, blank=True)   # 위도
    longitude = models.FloatField(null=True, blank=True)  # 경도
    cover_image = models.ImageField(upload_to='performance_images/', blank=True, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='performances'
    )
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.artist} ({self.date.date()})"

