from django.shortcuts import render

from based.generic_api.generic_api_views import GenericAPIView
from todolist.api.serializers import TaskRetrieveSerializer, TaskCreateSerializer, TagRetrieveSerializer, \
    TagCreateSerializer
from todolist.models import Task, Tag


# Create your views here.


class TaskAPI(GenericAPIView):


    serializer_class = TaskRetrieveSerializer

    queryset = Task.objects.detail()
    SERIALIZER = {
        "create": {
            "request": TaskCreateSerializer,
            "response": TaskRetrieveSerializer,
        },
        "list": {
            "request": None,
            "response": TaskRetrieveSerializer
        },
        "retrieve": {
            "request": None,
            "response": TaskRetrieveSerializer
        },
        "partial_update": {
            "request": TaskCreateSerializer,
            "response": TaskRetrieveSerializer,
        },
        "update": {
            "request": TaskCreateSerializer,
            "response": TaskRetrieveSerializer,
        }
    }


    def get_queryset(self):

        queryset = super().get_queryset().filter(user=self.request.user)
        if self.request.user.username == 'bot':
            if self.request.GET.get('tg_id'):
                queryset = queryset.filter(telegram_id=self.request.GET.get('tg_id'))

        return queryset

class TagsAPI(GenericAPIView):

    queryset = Tag.objects.all()

    serializer_class = TagRetrieveSerializer


    SERIALIZER = {
        "create": {
            "request": TagCreateSerializer,
            "response": TagRetrieveSerializer,
        },
        "list": {
            "request": None,
            "response": TagRetrieveSerializer
        },
        "retrieve": {
            "request": None,
            "response": TagRetrieveSerializer
        },
        "partial_update": {
            "request": TagCreateSerializer,
            "response": TagRetrieveSerializer,
        },
        "update": {
            "request": TagCreateSerializer,
            "response": TagRetrieveSerializer,
        }
    }