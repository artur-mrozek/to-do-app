from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Task(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    done = models.BooleanField(default=False)