from django.urls import include, path
from .views import ListApps, Company

urlpatterns = [
    path('apps/', ListApps.as_view(), name='app_list'),
    path('company/', Company.as_view(), name='company')
]