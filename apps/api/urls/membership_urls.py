from django.urls import path

from apps.api.views.membership_views import (
    add_membership, delete_membership, membership_by_id, membership_list_view,
    update_membership,
)

urlpatterns = [
     path('', membership_list_view),
     path('<int:pk>', membership_by_id),
     path('create', add_membership),
     path('<int:pk>/update', update_membership),
     path('<int:pk>/delete', delete_membership),
]
