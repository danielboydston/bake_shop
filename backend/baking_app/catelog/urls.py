from django.urls import path
from . import views

app_name = "catelog"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    #path("<int:pk>/item/", views.ItemIndexView.as_view(), name="itemindex"),
    #path("<int:pk>/item/<int:pk>", views.ItemDetailView.as_view(), name="detail")
]