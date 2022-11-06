from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.response import Response

from config_model.models import DictConfig

from .serializers import (DictConfigSerializerReadOnly,
                          DictConfigSerializerWriteOnly)


class DictConfigViewSet(viewsets.ModelViewSet):
    queryset = DictConfig.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ("id",)

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DictConfigSerializerReadOnly
        return DictConfigSerializerWriteOnly

    def destroy(self, request, *args, **kwargs):
        config = self.get_object()
        if config.in_use_indicator == "active":
            return Response(data='Нельзя удалить, конфигурация используется приложением')
        config.delete()
        return Response(data='Конфиг удален')
