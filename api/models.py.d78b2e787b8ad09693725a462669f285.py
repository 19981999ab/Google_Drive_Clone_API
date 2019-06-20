from django.db import models
from django.contrib.auth.models import User


class File(models.Model):
    owner = models.CharField(max_length=100, default="Anonymous")
    file = models.FileField(null=True, blank=True)
    name = models.CharField(max_length=100, default="default")

    def __str__(self):
        return self.file.name
