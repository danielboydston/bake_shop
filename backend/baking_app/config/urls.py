from django.urls import include, path
from .views import ListApps

urlpatterns = [
    path('apps/', ListApps.as_view(), name='app_list')
]