from django.db import models
from django.contrib.auth.models import User


class File(models.Model):
    owner = models.CharField(max_length=100, default="Anonymous")
    name = models.CharField(max_length=100, default="default")
    file = models.FileField(default="null")
    file_url = models.URLField(default="https://en.wikipedia.org/wiki/Rickrolling")

    def __str__(self):
        return self.name
