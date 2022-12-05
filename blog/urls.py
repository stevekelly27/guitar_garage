from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostList, name="home"),
    path("post_details", views.PostDetail, name="post_details")
]
