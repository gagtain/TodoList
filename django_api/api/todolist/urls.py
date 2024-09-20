
from django.contrib import admin
from django.urls import path

from todolist.api.views import TaskAPI, TagsAPI

urlpatterns = [
    path("tasks", TaskAPI.as_view({'post': 'create', 'get': 'list'})),
    path("tasks/<str:id>", TaskAPI.as_view({'delete': 'destroy',
                                            'get': 'retrieve',
                                            'patch': 'partial_update',
                                            'put': 'update'})),
    path("tags", TagsAPI.as_view({'post': 'create', 'get': 'list'})),
    path("tags/<str:id>", TagsAPI.as_view({'delete': 'destroy',
                                            'get': 'retrieve',
                                            'patch': 'partial_update',
                                            'put': 'update'}))
]
