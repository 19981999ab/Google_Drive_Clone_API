from django.db import models
from django.contrib.auth.models import User


class File(models.Model):
    owner = models.CharField(max_length=100, default="Anonymous")
<<<<<<< HEAD
    name = models.CharField(max_length=100, default="default")
    file = models.FileField(default="null")
    file_url = models.URLField(default="https://en.wikipedia.org/wiki/Rickrolling")

    def __str__(self):
        return self.name
=======
    file = models.FileField(null=True, blank=True)
    name = models.CharField(max_length=100, default="default")

    def __str__(self):
        return self.file.name
>>>>>>> c37e12077c7cf2e5a934d4397ea216a6079411f9
