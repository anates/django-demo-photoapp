from . import models
from rest_framework import mixins, viewsets

from django_large_image.rest import LargeImageFileDetailMixin

class ImageFileDetailViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
    LargeImageFileDetailMixin,
):
    queryset = models.ImageFile.objects.all()
    serializer_class = models.ImageFileSerializer

    FILE_FIELD_NAME = 'file'