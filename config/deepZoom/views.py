from django.shortcuts import render
from django_large_image.rest import LargeImageFileDetailMixin

# Create your views here.
class MyModelViewSet(viewsets.GenericViewSet, LargeImageFileDetailMixin):
    FILE_FIELD_NAME = 'field_name'

    