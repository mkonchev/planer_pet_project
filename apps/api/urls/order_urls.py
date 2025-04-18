from django.urls import path

from apps.api.views.order_views import order_list_view

urlpatterns = [
     path('', order_list_view),
]
