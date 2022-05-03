from django.contrib import admin

from .models import ImageFile

# Register your models here.

@admin.register(ImageFile)
class ImageFileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')