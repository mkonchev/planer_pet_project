from django.urls import path

from apps.api.views.order_views import order_by_id, order_list_view

urlpatterns = [
     path('', order_list_view),
     path('<int:pk>', order_by_id),
]
