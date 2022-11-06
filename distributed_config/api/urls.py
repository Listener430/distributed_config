from django.urls import include, path
from rest_framework import routers

from .views import DictConfigViewSet

router = routers.DefaultRouter()
router.register(r"config", DictConfigViewSet)

urlpatterns = [
    path("", include(router.urls), name="api_urls"),
]
