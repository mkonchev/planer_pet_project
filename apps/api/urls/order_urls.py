from django.urls import path

from apps.api.views.order_views import (
    add_order, delete_order, order_by_id, order_list_view, update_order,
)

urlpatterns = [
     path('', order_list_view),
     path('<int:pk>', order_by_id),
     path('create', add_order),
     path('<int:pk>/update', update_order),
     path('<int:pk>/delete', delete_order),
]
