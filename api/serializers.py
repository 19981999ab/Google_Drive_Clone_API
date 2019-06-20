from rest_framework import serializers
from .models import File
from django.forms.fields import FileField


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ("pk", "file", "name", "owner", "file_url")
