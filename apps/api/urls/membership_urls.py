from django.urls import path

from apps.api.views.membership_views import membership_list_view

urlpatterns = [
     path('', membership_list_view),
]
