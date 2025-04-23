from django.urls import path

from apps.api.views.group_views import (
    add_group, delete_group, group_by_id, group_by_slug, group_list_view,
    update_group,
)

urlpatterns = [
     path('', group_list_view),
     path('<int:pk>', group_by_id),
    #  path('<str:slug>', group_by_slug),
     path('create', add_group),
     path('<int:pk>/update', update_group),
     path('<int:pk>/delete', delete_group),
]
