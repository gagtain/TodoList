from typing import Optional

from rest_framework import mixins, viewsets, serializers, status
from rest_framework.response import Response

from users.models import TodoUser


class CommonAPIView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    Базовый класс для обработки запросов по API. (Класс для определения новых методов)
    """

    # Словарь с сериализаторами для запроса и ответа.
    # Пример: {'create': {'request': Serializer, 'response': Serializer}}
    # По умолчанию используется serializer_class
    SERIALIZER = {}
    lookup_field = "id"


class GenericAPIView(CommonAPIView):
    """
    Класс для обработки запросов по API. (Класс для переопределения методов DRF)
    """

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = self.get_serializer_response(obj)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


    def perform_create(self, serializer):
        return serializer.save()


    def get_serializer_class(self, *args, **kwargs) -> Optional[serializers.Serializer] | dict:
        """Возвращает класс сериализатора для запроса"""

        if self.action in ['retrieve', 'list']:
            return self.SERIALIZER.get(self.action).get("response", self.serializer_class)



        if self.serializer_class is None:
            return None

        if self.action not in self.SERIALIZER:
            return self.serializer_class


        return self.SERIALIZER.get(self.action).get("request", self.serializer_class)

    def get_serializer_response(self, instance, **kwargs) -> dict:
        """Возвращает сериализованный объект"""

        if self.action not in self.SERIALIZER:
            return self.serializer_class(instance, **kwargs).data  # pylint: disable=not-callable

        return self.SERIALIZER.get(self.action).get("response", self.serializer_class)(instance, **kwargs).data
