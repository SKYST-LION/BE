from django.db import models
from django.conf import settings

class Artist(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='artists'
    )
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_artists', blank=True)

    def like_count(self):
        return self.likes.count()

    def __str__(self):
        return self.name