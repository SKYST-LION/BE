from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    nickname = models.CharField(max_length=30, blank = True)
    provider = models.CharField(max_length=20, blank = True)

    def __str__(self):
        return self.nickname
