from django.urls import path

from apps.api.views.group_views import group_list_view

urlpatterns = [
     path('', group_list_view),
]
