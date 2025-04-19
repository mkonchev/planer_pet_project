from django.urls import path

from apps.api.views.membership_views import (
    membership_by_id, membership_list_view,
)

urlpatterns = [
     path('', membership_list_view),
     path('<int:pk>', membership_by_id),
]
