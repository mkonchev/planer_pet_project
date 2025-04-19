from django.urls import path

from apps.api.views.task_views import task_by_id, task_list_view

urlpatterns = [
     path('', task_list_view),
     path('<int:pk>', task_by_id),
]
