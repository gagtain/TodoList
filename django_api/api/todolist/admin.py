from django.contrib import admin

from todolist.models import Tag, Task


# Register your models here.

admin.site.register(Task)
admin.site.register(Tag)