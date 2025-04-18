from django.urls import path

from apps.api.views.group_views import group_by_id, group_list_view

urlpatterns = [
     path('', group_list_view),
     path('<int:pk>', group_by_id),
]
