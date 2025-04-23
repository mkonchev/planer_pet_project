from django.urls import path

from apps.api.views.store_views import (
    add_store, delete_store, store_by_id, store_list_view,
)

urlpatterns = [
     path('', store_list_view),
     path('<int:pk>', store_by_id),
     path('create', add_store),
     path('<int:pk>/update', add_store),
     path('<int:pk>/delete', delete_store),
]
