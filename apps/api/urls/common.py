from django.urls import include, path

app_name = 'api'

urlpatterns = [
     path('groups/', include('apps.api.urls.group_urls')),
     path('users/', include('apps.api.urls.user_urls')),
     path('memberships/', include('apps.api.urls.membership_urls')),
     path('orders/', include('apps.api.urls.order_urls')),
     path('tasks/', include('apps.api.urls.task_urls')),
]
