from django.core.cache import cache
from django.db import models

from based.models import BaseModel
from todolist.selectors import TaskQuerySet
from users.models import TodoUser


# Create your models here.


class Tag(BaseModel):
    name = models.CharField(max_length=128)


class Task(BaseModel):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True)
    user = models.ForeignKey(TodoUser, related_name="task_list", on_delete=models.SET_NULL, null=True)
    telegram_id = models.CharField(max_length=128, null=True)
    tag_list = models.ManyToManyField(Tag, related_name="task_list")

    dead_line_time = models.DateTimeField(null=True)
    is_notify = models.BooleanField(default=False)


    objects = TaskQuerySet.as_manager()


    def delete(self, using=None, keep_parents=False):

        cache.set(str(self.id), "false", 60 * 10)
        return super().delete(using, keep_parents)
