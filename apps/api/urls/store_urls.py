from django.urls import path

from apps.api.views.store_views import store_list_view

urlpatterns = [
     path('', store_list_view),
]
