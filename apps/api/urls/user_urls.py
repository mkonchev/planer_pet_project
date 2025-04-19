from django.urls import path

from apps.api.views.user_views import (  # user_by_username,
    user_by_id, user_list_view,
)

urlpatterns = [
     path('', user_list_view),
     path('<int:pk>', user_by_id),
     # path('<str:username>', user_by_username),
]
