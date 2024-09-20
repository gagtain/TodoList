from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/todo_list/', include('todolist.urls')),
    path('api/users/', include('users.urls'))
]
