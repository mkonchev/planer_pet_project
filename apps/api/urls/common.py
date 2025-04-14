from django.urls import include, path

app_name = 'api'

urlpatterns = [
     path('groups/', include('apps.api.urls.group_urls')),
]
