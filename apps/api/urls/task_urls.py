from django.urls import path

from apps.api.views.task_views import (
    add_task, delete_task, task_by_id, task_list_view, update_task,
)

urlpatterns = [
     path('', task_list_view),
     path('<int:pk>', task_by_id),
     path('create', add_task),
     path('<int:pk>/update', update_task),
     path('<int:pk>/delete', delete_task),
]
