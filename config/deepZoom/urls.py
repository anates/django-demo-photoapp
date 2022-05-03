from lib2to3.pgen2.literals import simple_escapes
from django.urls import path
from rest_framework.routers import SimpleRouter

from .viewsets import ImageFileDetailViewSet

app_name = "deepZoom"

router = SimpleRouter(trailing_slash = False)
router.register(r'api/image-file', ImageFileDetailViewSet)

urlpatterns = [
    path('', include('django_large_image.urls'))
] + router.urls