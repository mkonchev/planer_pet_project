from django.urls import include, path

app_name = 'api'

urlpatterns = [
     path('group/', include('apps.api.urls.group_urls')),
     path('user/', include('apps.api.urls.user_urls')),
     path('membership/', include('apps.api.urls.membership_urls')),
     path('order/', include('apps.api.urls.order_urls')),
     path('task/', include('apps.api.urls.task_urls')),
     path('store/', include('apps.api.urls.store_urls')),
]
