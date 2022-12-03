from django.urls import path
from . import views

rlpatterns = [
    path("", views.PostList.as_view(), name="home"),
]