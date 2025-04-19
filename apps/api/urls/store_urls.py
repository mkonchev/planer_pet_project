from django.urls import path

from apps.api.views.store_views import store_by_id, store_list_view

urlpatterns = [
     path('', store_list_view),
     path('<int:pk>', store_by_id),
]
