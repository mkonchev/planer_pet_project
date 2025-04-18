from django.urls import path

from apps.api.views.user_views import user_list_view

urlpatterns = [
     path('', user_list_view),
]
