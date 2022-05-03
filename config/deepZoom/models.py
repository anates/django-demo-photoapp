from django.db import models
from rest_framework import serializers

# Create your models here.

class ImageFile(models.Model):
    name = models.TextField()
    file = models.FileField()

class ImageFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageFile
        fields = '__all__'
