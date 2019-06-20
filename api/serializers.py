from rest_framework import serializers
from .models import File
<<<<<<< HEAD
from django.forms.fields import FileField
=======
>>>>>>> c37e12077c7cf2e5a934d4397ea216a6079411f9


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
<<<<<<< HEAD
        fields = ("pk", "file", "name", "owner", "file_url")
=======
        fields = ("file", "name", "owner")

>>>>>>> c37e12077c7cf2e5a934d4397ea216a6079411f9
