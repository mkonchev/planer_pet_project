from django.urls import path

from apps.api.views.user_views import (  # user_by_username,
    add_user, delete_user, update_user, user_by_id, user_list_view,
)

urlpatterns = [
     path('', user_list_view),
     path('<int:pk>', user_by_id),
     # path('<str:username>', user_by_username),
     path('create', add_user),
     path('<int:pk>/update', update_user),
     path('<int:pk>/delete', delete_user),
]
